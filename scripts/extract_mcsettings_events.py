#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_mcsettings_events.py

Purpose:
  Extract MCState / ManagedSettings / DMD / Digital Health / Game Center
  restriction evidence from preserved private sysdiagnose archives.

What it does:
  - Recursively scans a private artifact directory.
  - Reads loose sysdiagnose .tar.gz files.
  - Reads sysdiagnose .tar.gz files embedded inside ZIP archives.
  - Extracts selected plist / text targets:
      - CloudConfigurationDetails.plist
      - MCProfileEvents.plist
      - PayloadManifest.plist
      - EffectiveUserSettings.plist
      - MCSettingsEvents.plist
      - ManagedSettings SafariStore
      - ScreenTimeEnabled_CurrentUser.txt
      - brctl dump
      - Wi-Fi / networking text summaries
  - Outputs:
      - visible management summary
      - EffectiveUserSettings selected values
      - SafariStore state
      - MCSettingsEvents flattened timeline
      - Game Center restriction rows
      - FileProvider / iCloud Drive state markers
      - JSON and CSV output

Safety boundary:
  - Reads local preserved artifacts only.
  - Does not modify artifacts.
  - Does not connect to devices.
  - Does not perform network activity.
  - Does not install profiles.
  - Does not alter Apple ID / iCloud / Screen Time state.

Example:
  python extract_mcsettings_events.py --input private_artifacts --output review_output/mcsettings_events
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import plistlib
import re
import sys
import tarfile
import tempfile
import zipfile
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


TARGET_SUFFIXES = {
    "cloud_config": "logs/MCState/Shared/CloudConfigurationDetails.plist",
    "mc_profile_events": "logs/MCState/Shared/MCProfileEvents.plist",
    "payload_manifest": "logs/MCState/Shared/PayloadManifest.plist",
    "effective_user_settings": "logs/MCState/User/EffectiveUserSettings.plist",
    "mc_settings_events": "logs/MCState/Shared/MCSettingsEvents.plist",
    "managedsettings_effective": "logs/ManagedSettings/EffectiveSettings.plist",
    "managedsettings_setting_records": "logs/ManagedSettings/SettingRecords.plist",
    "safari_store": "logs/ManagedSettings/com.apple.ScreenTime/SafariStore.plist",
    "client_effective_settings": "logs/ManagedSettings/com.apple.ScreenTime/clientEffectiveSettings.plist",
    "user_safety": "logs/ManagedSettings/com.apple.Preferences/UserSafety.plist",
    "screentime_enabled": "Preferences/ScreenTimeEnabled_CurrentUser.txt",
    "brctl_dump": "brctl/brctl-dump.txt",
    "bird_defaults": "brctl/defaults-com.apple.bird.txt",
    "wifi_status": "WiFi/wifi_status.txt",
    "network_status": "WiFi/network_status.txt",
    "wifi_scan": "WiFi/wifi_scan.txt",
    "route_info": "logs/Networking/route-info.txt",
    "skywalk": "logs/Networking/skywalk.txt",
    "sysctl": "sysctl.txt",
}

SELECTED_RESTRICTION_KEYS = [
    "allowAccountModification",
    "allowScreenTimeModification",
    "allowMDMEnrollment",
    "allowUIConfigurationProfileInstallation",
    "allowScreenShot",
    "allowScreenRecording",
    "allowSafariPrivateBrowsing",
    "allowSafariHistoryClearing",
    "forceAutomaticDateAndTime",
    "allowPasswordSharing",
    "allowWiFiPasswordSharing",
    "allowGeotagSharing",
    "allowSelectedTextSharing",
    "allowSharedStream",
    "allowSharedDeviceTemporarySession",
    "allowAddingGameCenterFriends",
    "allowGameCenterFriendsSharingModification",
    "allowGameCenterPrivateMessaging",
    "allowGameCenterProfileModification",
    "allowGameCenterProfilePrivacyModification",
    "allowGameCenterNearbyMultiplayer",
    "allowMultiplayerGaming",
    "allowGameCenter",
]

SELECTED_VALUE_KEYS = [
    "allowedGameCenterOtherPlayerTypes",
    "ratingApps",
    "ratingMovies",
    "ratingTVShows",
]


@dataclass
class SysdiagnoseSummary:
    source: str
    sha256_16: str
    cloud_config_present: bool
    is_supervised: str
    post_setup_profile_was_installed: str
    cloud_configuration_ui_complete: str
    configuration_source: str
    allow_pairing: str
    mc_profile_events_status: str
    payload_manifest_status: str
    effective_user_settings_present: bool
    managedsettings_present: bool
    safari_store_present: bool
    screentime_enabled_current_user: str
    brctl_icloud_not_configured: bool
    lockdown_mode_state: str
    wifi_ssid_state: str
    wifi_rssi_state: str
    primary_ipv4_state: str
    apple_network_state: str


@dataclass
class RestrictionRow:
    source: str
    key: str
    value_type: str
    value: str
    source_section: str


@dataclass
class SafariStoreRow:
    source: str
    deny_private_browsing: str
    deny_history_clearing: str
    active: str
    raw_keys: str


@dataclass
class MCEventRow:
    source: str
    timestamp: str
    process: str
    event: str
    path: str
    value_summary: str


@dataclass
class GameCenterRow:
    source: str
    timestamp: str
    process: str
    event: str
    path: str
    value_summary: str


@dataclass
class TextMarkerRow:
    source: str
    marker: str
    present: bool
    count: int
    file_key: str


def sha256_16(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:16]


def safe_decode(data: bytes) -> str:
    return data.decode("utf-8", "replace")


def load_plist(data: Optional[bytes]) -> Any:
    if not data:
        return None
    try:
        return plistlib.loads(data)
    except Exception:
        return None


def text_value(data: Optional[bytes]) -> str:
    if not data:
        return ""
    return safe_decode(data).strip()


def as_str(v: Any) -> str:
    if v is None:
        return ""
    if isinstance(v, (dict, list)):
        return json.dumps(v, ensure_ascii=False, sort_keys=True)
    return str(v)


def find_label(text: str, label: str) -> str:
    m = re.search(rf"^{re.escape(label)}\s*:\s*(.*)$", text, re.MULTILINE)
    return m.group(1).strip() if m else ""


def iter_sysdiagnose_sources(input_dir: Path) -> Iterable[Tuple[str, bytes]]:
    for p in sorted(input_dir.rglob("*.tar.gz")):
        if not p.is_file():
            continue
        try:
            yield str(p.relative_to(input_dir)), p.read_bytes()
        except Exception as e:
            print(f"[WARN] Cannot read tar.gz {p}: {e}", file=sys.stderr)

    for zip_path in sorted(input_dir.rglob("*.zip")):
        try:
            with zipfile.ZipFile(zip_path) as z:
                for name in z.namelist():
                    if name.endswith("/") or not name.endswith(".tar.gz"):
                        continue
                    if "sysdiagnose_" not in Path(name).name:
                        continue
                    try:
                        data = z.read(name)
                        source = f"{zip_path.relative_to(input_dir)}::{name}"
                        yield source, data
                    except Exception as e:
                        print(f"[WARN] Cannot read embedded sysdiagnose {zip_path}:{name}: {e}", file=sys.stderr)
        except Exception as e:
            print(f"[WARN] Cannot read zip {zip_path}: {e}", file=sys.stderr)


def extract_targets_from_tar(data: bytes) -> Dict[str, bytes]:
    found: Dict[str, bytes] = {}

    try:
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
            for m in tar:
                if not m.isfile():
                    continue

                for key, suffix in TARGET_SUFFIXES.items():
                    if m.name.endswith(suffix):
                        try:
                            f = tar.extractfile(m)
                            if f:
                                found[key] = f.read()
                        except Exception:
                            pass
                        break

    except Exception as e:
        print(f"[WARN] Cannot parse sysdiagnose tar: {e}", file=sys.stderr)

    return found


def payload_manifest_status(obj: Any) -> str:
    if obj is None:
        return "missing"

    if isinstance(obj, dict):
        ordered = obj.get("OrderedProfiles")
        hidden = obj.get("HiddenProfiles")
        if ordered == [] and hidden == []:
            return "empty"
        return f"present:{json.dumps(obj, ensure_ascii=False, sort_keys=True)[:300]}"

    return "present_non_dict"


def mc_profile_events_status(obj: Any) -> str:
    if obj is None:
        return "missing"
    if obj == []:
        return "empty"
    return f"present:{json.dumps(obj, ensure_ascii=False, sort_keys=True)[:300]}"


def get_restricted_bool_value(eff: Any, key: str) -> str:
    if not isinstance(eff, dict):
        return ""
    rb = eff.get("restrictedBool", {})
    if not isinstance(rb, dict) or key not in rb:
        return ""

    v = rb[key]
    if isinstance(v, dict):
        if "value" in v:
            return as_str(v.get("value"))
        return as_str(v)
    return as_str(v)


def get_restricted_value(eff: Any, key: str) -> str:
    if not isinstance(eff, dict):
        return ""
    rv = eff.get("restrictedValue", {})
    if not isinstance(rv, dict) or key not in rv:
        return ""
    return as_str(rv[key])


def build_restriction_rows(source: str, eff: Any) -> List[RestrictionRow]:
    rows: List[RestrictionRow] = []

    for key in SELECTED_RESTRICTION_KEYS:
        value = get_restricted_bool_value(eff, key)
        rows.append(
            RestrictionRow(
                source=source,
                key=key,
                value_type="restrictedBool",
                value=value,
                source_section="EffectiveUserSettings",
            )
        )

    for key in SELECTED_VALUE_KEYS:
        value = get_restricted_value(eff, key)
        rows.append(
            RestrictionRow(
                source=source,
                key=key,
                value_type="restrictedValue",
                value=value,
                source_section="EffectiveUserSettings",
            )
        )

    return rows


def build_safari_row(source: str, safari: Any) -> SafariStoreRow:
    if not isinstance(safari, dict):
        return SafariStoreRow(
            source=source,
            deny_private_browsing="",
            deny_history_clearing="",
            active="",
            raw_keys="",
        )

    return SafariStoreRow(
        source=source,
        deny_private_browsing=as_str(safari.get("safari.denyPrivateBrowsing")),
        deny_history_clearing=as_str(safari.get("safari.denyHistoryClearing")),
        active=as_str(safari.get("active")),
        raw_keys=";".join(sorted(str(k) for k in safari.keys())),
    )


def summarize_value(x: Any) -> str:
    if isinstance(x, dict):
        keys = sorted(str(k) for k in x.keys())
        if "value" in x:
            return f"value={x.get('value')} keys={keys}"
        return f"dict_keys={keys}"
    if isinstance(x, list):
        return f"list_len={len(x)}"
    return as_str(x)


def flatten_mc_events(source: str, obj: Any) -> List[MCEventRow]:
    rows: List[MCEventRow] = []

    def walk(x: Any, path: str = "") -> None:
        if isinstance(x, dict):
            if {"timestamp", "process", "event"} <= set(x.keys()):
                rows.append(
                    MCEventRow(
                        source=source,
                        timestamp=as_str(x.get("timestamp")),
                        process=as_str(x.get("process")),
                        event=as_str(x.get("event")),
                        path=path,
                        value_summary=summarize_value(x.get("value", x.get("payload", ""))),
                    )
                )

            for k, v in x.items():
                child = f"{path}.{k}" if path else str(k)
                walk(v, child)

        elif isinstance(x, list):
            for i, v in enumerate(x):
                child = f"{path}[{i}]"
                walk(v, child)

    walk(obj)
    return sorted(rows, key=lambda r: (r.timestamp, r.path))


def build_gamecenter_rows(events: List[MCEventRow]) -> List[GameCenterRow]:
    out: List[GameCenterRow] = []
    for r in events:
        hay = f"{r.path} {r.value_summary}".lower()
        if "gamecenter" in hay or "game center" in hay or "multiplayer" in hay:
            out.append(
                GameCenterRow(
                    source=r.source,
                    timestamp=r.timestamp,
                    process=r.process,
                    event=r.event,
                    path=r.path,
                    value_summary=r.value_summary,
                )
            )
    return out


def build_summary(source: str, sha: str, found: Dict[str, bytes]) -> SysdiagnoseSummary:
    cloud = load_plist(found.get("cloud_config"))
    profile_events = load_plist(found.get("mc_profile_events"))
    payload = load_plist(found.get("payload_manifest"))
    eff = load_plist(found.get("effective_user_settings"))
    safari = load_plist(found.get("safari_store"))

    network_status = text_value(found.get("network_status"))
    wifi_status = text_value(found.get("wifi_status"))
    brctl = text_value(found.get("brctl_dump"))
    sysctl = text_value(found.get("sysctl"))
    screentime = text_value(found.get("screentime_enabled"))

    lockdown = ""
    m = re.search(r"lockdown_mode_state\s*:\s*(\S+)", sysctl)
    if m:
        lockdown = m.group(1)

    return SysdiagnoseSummary(
        source=source,
        sha256_16=sha,
        cloud_config_present=isinstance(cloud, dict),
        is_supervised=as_str(cloud.get("IsSupervised")) if isinstance(cloud, dict) else "",
        post_setup_profile_was_installed=as_str(cloud.get("PostSetupProfileWasInstalled")) if isinstance(cloud, dict) else "",
        cloud_configuration_ui_complete=as_str(cloud.get("CloudConfigurationUIComplete")) if isinstance(cloud, dict) else "",
        configuration_source=as_str(cloud.get("ConfigurationSource")) if isinstance(cloud, dict) else "",
        allow_pairing=as_str(cloud.get("AllowPairing")) if isinstance(cloud, dict) else "",
        mc_profile_events_status=mc_profile_events_status(profile_events),
        payload_manifest_status=payload_manifest_status(payload),
        effective_user_settings_present=isinstance(eff, dict),
        managedsettings_present=any(k.startswith("managedsettings") or k in {"safari_store", "client_effective_settings", "user_safety"} for k in found),
        safari_store_present=isinstance(safari, dict),
        screentime_enabled_current_user=screentime,
        brctl_icloud_not_configured=("Logged out - iCloud Drive is not configured" in brctl),
        lockdown_mode_state=lockdown,
        wifi_ssid_state=find_label(wifi_status, "SSID"),
        wifi_rssi_state=find_label(wifi_status, "RSSI"),
        primary_ipv4_state=find_label(network_status, "Primary IPv4"),
        apple_network_state=find_label(network_status, "Apple"),
    )


def build_text_markers(source: str, found: Dict[str, bytes]) -> List[TextMarkerRow]:
    markers = [
        ("icloud_not_configured", "Logged out - iCloud Drive is not configured", "brctl_dump"),
        ("needs_auth", "needs-auth", "brctl_dump"),
        ("fileprovider", "fileprovider", "brctl_dump"),
        ("CloudDocs", "CloudDocs", "brctl_dump"),
        ("ScreenTimeEnabled_empty", "{}", "screentime_enabled"),
        ("en0_route", "en0", "route_info"),
        ("pdp_ip0_route", "pdp_ip0", "route_info"),
        ("Apple_WWAN", "WWAN", "network_status"),
        ("Apple_WiFi", "Wi-Fi", "network_status"),
    ]

    rows: List[TextMarkerRow] = []
    for marker_name, needle, file_key in markers:
        text = text_value(found.get(file_key))
        count = text.count(needle)
        rows.append(
            TextMarkerRow(
                source=source,
                marker=marker_name,
                present=count > 0,
                count=count,
                file_key=file_key,
            )
        )
    return rows


def write_csv(path: Path, rows: List[Any], fieldnames: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in rows:
            if hasattr(row, "__dataclass_fields__"):
                w.writerow(asdict(row))
            else:
                w.writerow(row)


def write_json(path: Path, rows: List[Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    out = []
    for row in rows:
        out.append(asdict(row) if hasattr(row, "__dataclass_fields__") else row)
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")


def write_markdown_summary(
    path: Path,
    summaries: List[SysdiagnoseSummary],
    safari_rows: List[SafariStoreRow],
    gamecenter_rows: List[GameCenterRow],
    events: List[MCEventRow],
) -> None:
    lines: List[str] = []
    lines.append("# MCSettings Extraction Summary")
    lines.append("")
    lines.append("## Sysdiagnose summaries")
    for s in summaries:
        lines.append(f"### {s.source}")
        lines.append("")
        lines.append(f"- sha256_16: `{s.sha256_16}`")
        lines.append(f"- IsSupervised: `{s.is_supervised}`")
        lines.append(f"- PostSetupProfileWasInstalled: `{s.post_setup_profile_was_installed}`")
        lines.append(f"- MCProfileEvents: `{s.mc_profile_events_status}`")
        lines.append(f"- PayloadManifest: `{s.payload_manifest_status}`")
        lines.append(f"- EffectiveUserSettings present: `{s.effective_user_settings_present}`")
        lines.append(f"- SafariStore present: `{s.safari_store_present}`")
        lines.append(f"- ScreenTimeEnabled_CurrentUser: `{s.screentime_enabled_current_user}`")
        lines.append(f"- brctl iCloud not configured: `{s.brctl_icloud_not_configured}`")
        lines.append(f"- Primary IPv4: `{s.primary_ipv4_state}`")
        lines.append(f"- Apple network: `{s.apple_network_state}`")
        lines.append("")

    lines.append("## SafariStore rows")
    for r in safari_rows:
        lines.append(
            f"- `{r.source}` denyPrivateBrowsing=`{r.deny_private_browsing}` "
            f"denyHistoryClearing=`{r.deny_history_clearing}` active=`{r.active}`"
        )
    lines.append("")

    lines.append("## Game Center event rows")
    for r in gamecenter_rows:
        lines.append(f"- `{r.timestamp}` `{r.process}` `{r.event}` `{r.path}`")
    lines.append("")

    lines.append("## 2026-03-05 11:00-11:40 MCSettingsEvents")
    for r in events:
        if r.timestamp.startswith("2026-03-05 11:"):
            minute = r.timestamp[14:16] if len(r.timestamp) >= 16 else ""
            if minute.isdigit() and 0 <= int(minute) <= 40:
                lines.append(f"- `{r.timestamp}` `{r.process}` `{r.event}` `{r.path}`")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Private artifact directory")
    ap.add_argument("--output", required=True, help="Output directory")
    args = ap.parse_args()

    in_dir = Path(args.input)
    out_dir = Path(args.output)

    if not in_dir.exists():
        print(f"[ERROR] input does not exist: {in_dir}", file=sys.stderr)
        return 2

    summaries: List[SysdiagnoseSummary] = []
    restrictions: List[RestrictionRow] = []
    safari_rows: List[SafariStoreRow] = []
    events: List[MCEventRow] = []
    gamecenter_rows: List[GameCenterRow] = []
    markers: List[TextMarkerRow] = []

    count = 0

    for source, data in iter_sysdiagnose_sources(in_dir):
        count += 1
        sha = sha256_16(data)
        found = extract_targets_from_tar(data)

        summary = build_summary(source, sha, found)
        summaries.append(summary)

        eff = load_plist(found.get("effective_user_settings"))
        restrictions.extend(build_restriction_rows(source, eff))

        safari = load_plist(found.get("safari_store"))
        safari_rows.append(build_safari_row(source, safari))

        mc_events_obj = load_plist(found.get("mc_settings_events"))
        event_rows = flatten_mc_events(source, mc_events_obj)
        events.extend(event_rows)
        gamecenter_rows.extend(build_gamecenter_rows(event_rows))

        markers.extend(build_text_markers(source, found))

    write_csv(out_dir / "sysdiagnose_summary.csv", summaries, list(SysdiagnoseSummary.__dataclass_fields__.keys()))
    write_json(out_dir / "sysdiagnose_summary.json", summaries)

    write_csv(out_dir / "effective_user_settings_selected.csv", restrictions, list(RestrictionRow.__dataclass_fields__.keys()))
    write_json(out_dir / "effective_user_settings_selected.json", restrictions)

    write_csv(out_dir / "safari_store.csv", safari_rows, list(SafariStoreRow.__dataclass_fields__.keys()))
    write_json(out_dir / "safari_store.json", safari_rows)

    write_csv(out_dir / "mcsettings_events.csv", events, list(MCEventRow.__dataclass_fields__.keys()))
    write_json(out_dir / "mcsettings_events.json", events)

    write_csv(out_dir / "gamecenter_events.csv", gamecenter_rows, list(GameCenterRow.__dataclass_fields__.keys()))
    write_json(out_dir / "gamecenter_events.json", gamecenter_rows)

    write_csv(out_dir / "text_markers.csv", markers, list(TextMarkerRow.__dataclass_fields__.keys()))
    write_json(out_dir / "text_markers.json", markers)

    write_markdown_summary(out_dir / "summary.md", summaries, safari_rows, gamecenter_rows, events)

    print(f"[OK] sysdiagnose sources processed: {count}")
    print(f"[OK] wrote output to: {out_dir}")
    print(f"[OK] summaries: {len(summaries)}")
    print(f"[OK] restriction rows: {len(restrictions)}")
    print(f"[OK] MCSettingsEvents rows: {len(events)}")
    print(f"[OK] Game Center rows: {len(gamecenter_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
