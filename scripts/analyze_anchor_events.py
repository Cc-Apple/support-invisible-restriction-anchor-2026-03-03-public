#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
analyze_anchor_events.py

Purpose:
  Reproducibility helper for the public three-anchor review package.

What it does:
  - Recursively scans a private artifact directory.
  - Reads ZIP archives and loose .ips / .txt / .log style files.
  - Produces safe summary outputs:
      - file inventory
      - timeline
      - category counts
      - bug_type counts
      - disk-write summaries
      - stackshot memory summaries
      - selected Analytics / RTC / SFA keyword summaries

Safety boundary:
  - Reads local preserved artifacts only.
  - Does not modify artifacts.
  - Does not connect to devices.
  - Does not perform network activity.
  - Does not extract credentials.
  - Does not publish raw sensitive content.

Example:
  python analyze_anchor_events.py --input private_artifacts --output review_output/anchor_events
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import zipfile
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


TEXT_EXTENSIONS = {
    ".ips",
    ".synced",
    ".txt",
    ".log",
    ".session",
    ".spin",
    ".plist",
    ".json",
}

SELECTED_ANALYTICS_NAMES = {
    "MDMEnrollmentStatus_Powerlog",
    "LogWritingUsage",
    "LogRetirement",
    "LogRetirementV2",
    "LogSubmissionsByBugType",
    "JetsamAggregationV4",
    "PowerlogTaskingReport",
}

PROCESS_TERMS = [
    "fileprovider",
    "LocalStorageFileProvider",
    "CloudDocs",
    "cloudd",
    "bird",
    "deleted",
    "searchd",
    "triald",
    "parsecd",
    "suggestd",
    "duet",
    "coreduet",
    "appleaccount",
    "accountsd",
    "securityd",
    "akd",
    "trustd",
    "CommCenter",
    "corespeech",
    "localspeech",
    "FindMy",
    "Family",
    "familycircled",
    "ScreenTime",
    "DMD",
    "ManagedSettings",
    "WeChat",
    "ChatGPT",
    "DeepSeek",
    "Gemini",
    "Zalo",
    "Translate",
    "Chrome",
    "Gmail",
    "maild",
    "MobilePhone",
    "Alipay",
    "ScreenshotServicesService",
    "ANECompilerService",
    "sysdiagnosed",
    "Photos",
    "photoanalysisd",
    "mediaanalysisd",
    "spotlight",
    "VisualIntelligence",
]


@dataclass
class FileRow:
    source_archive: str
    inner_path: str
    filename: str
    category: str
    timestamp: str
    bug_type: str
    app_name: str
    process_name: str
    size_bytes: int
    sha256_16: str


@dataclass
class DiskWriteRow:
    source_archive: str
    filename: str
    timestamp: str
    date_time: str
    end_time: str
    process_or_path: str
    event: str
    writes: str
    free_disk_space: str
    on_behalf_of: str


@dataclass
class StackshotRow:
    source_archive: str
    filename: str
    timestamp: str
    free_pages: str
    purgeable_pages: str
    speculative_pages: str
    pages_wanted: str
    pages_reclaimed: str
    process_count: int
    found_terms: str


@dataclass
class KeywordRow:
    source_archive: str
    filename: str
    timestamp: str
    category: str
    keyword: str
    count: int


def sha256_16(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:16]


def safe_decode(data: bytes) -> str:
    return data.decode("utf-8", "replace")


def parse_json_header(text: str) -> Dict[str, Any]:
    first = text.splitlines()[0] if text.splitlines() else ""
    try:
        obj = json.loads(first)
        return obj if isinstance(obj, dict) else {}
    except Exception:
        return {}


def parse_json_body_after_header(text: str) -> Any:
    lines = text.splitlines()
    if len(lines) < 2:
        return None
    body_text = "\n".join(lines[1:]).strip()
    if not body_text:
        return None
    try:
        return json.loads(body_text)
    except Exception:
        return None


def classify_file(filename: str, inner_path: str) -> str:
    name = filename

    if name.startswith("Analytics-"):
        return "Analytics"
    if name.startswith("RTCReporting"):
        return "RTCReporting"
    if name.startswith("SFA-"):
        return "SFA"
    if name.startswith("SiriSearchFeedback"):
        return "SiriSearchFeedback"
    if name.startswith("JetsamEvent"):
        return "JetsamEvent"
    if name.startswith("stacks-"):
        return "stackshot"
    if "diskwrites_resource" in name:
        return "diskwrites_resource"
    if "cpu_resource" in name:
        return "cpu_resource"
    if name.startswith("WiFiConnectionQuality"):
        return "WiFiConnectionQuality"
    if name.startswith("xp_amp_app_usage_dnu"):
        return "xp_amp_app_usage_dnu"
    if name.startswith("sysdiagnose_") and name.endswith(".tar.gz"):
        return "sysdiagnose_archive"
    if "MCState" in inner_path:
        return "MCState"
    if "ManagedSettings" in inner_path:
        return "ManagedSettings"
    if "FileProvider" in inner_path:
        return "FileProvider"
    return "other"


def get_header_field(header: Dict[str, Any], *keys: str) -> str:
    for k in keys:
        v = header.get(k)
        if v is not None:
            return str(v)
    return ""


def iter_zip_text_files(zip_path: Path) -> Iterable[Tuple[str, bytes]]:
    try:
        with zipfile.ZipFile(zip_path) as z:
            for name in z.namelist():
                if name.endswith("/"):
                    continue

                filename = Path(name).name
                lower_name = filename.lower()

                if lower_name.endswith(".tar.gz"):
                    # Do not unpack sysdiagnose here. Dedicated MCSettings script handles it.
                    yield name, b"__SYSDIAGNOSE_ARCHIVE_PLACEHOLDER__"
                    continue

                if not any(lower_name.endswith(ext) for ext in TEXT_EXTENSIONS):
                    continue

                try:
                    yield name, z.read(name)
                except Exception:
                    continue
    except Exception as e:
        print(f"[WARN] Cannot read ZIP: {zip_path} : {e}", file=sys.stderr)


def iter_loose_text_files(root: Path) -> Iterable[Tuple[Path, bytes]]:
    for p in root.rglob("*"):
        if not p.is_file():
            continue

        lower_name = p.name.lower()

        if lower_name.endswith(".zip"):
            continue
        if lower_name.endswith(".tar.gz"):
            continue
        if not any(lower_name.endswith(ext) for ext in TEXT_EXTENSIONS):
            continue

        try:
            yield p, p.read_bytes()
        except Exception:
            continue


def extract_field_from_text(text: str, label: str) -> str:
    pattern = rf"^{re.escape(label)}\s*:\s*(.*)$"
    m = re.search(pattern, text, re.MULTILINE)
    return m.group(1).strip() if m else ""


def parse_diskwrite(source_archive: str, inner_path: str, text: str, header: Dict[str, Any]) -> DiskWriteRow:
    filename = Path(inner_path).name
    return DiskWriteRow(
        source_archive=source_archive,
        filename=filename,
        timestamp=get_header_field(header, "timestamp"),
        date_time=extract_field_from_text(text, "Date/Time"),
        end_time=extract_field_from_text(text, "End time"),
        process_or_path=extract_field_from_text(text, "Path"),
        event=extract_field_from_text(text, "Event"),
        writes=extract_field_from_text(text, "Writes"),
        free_disk_space=extract_field_from_text(text, "Free disk space"),
        on_behalf_of=extract_field_from_text(text, "On Behalf Of"),
    )


def parse_stackshot(source_archive: str, inner_path: str, text: str, header: Dict[str, Any]) -> Optional[StackshotRow]:
    filename = Path(inner_path).name
    body = parse_json_body_after_header(text)
    if not isinstance(body, dict):
        return None

    memory_status = body.get("memoryStatus", {}) or {}
    memory_pages = memory_status.get("memoryPages", {}) or {}
    pressure_details = memory_status.get("memoryPressureDetails", {}) or {}
    process_by_pid = body.get("processByPid", {}) or {}

    proc_text = json.dumps(process_by_pid, ensure_ascii=False)
    found = sorted({term for term in PROCESS_TERMS if term.lower() in proc_text.lower()})

    return StackshotRow(
        source_archive=source_archive,
        filename=filename,
        timestamp=get_header_field(header, "timestamp"),
        free_pages=str(memory_pages.get("free", "")),
        purgeable_pages=str(memory_pages.get("purgeable", "")),
        speculative_pages=str(memory_pages.get("speculative", "")),
        pages_wanted=str(pressure_details.get("pagesWanted", "")),
        pages_reclaimed=str(pressure_details.get("pagesReclaimed", "")),
        process_count=len(process_by_pid),
        found_terms=";".join(found),
    )


def count_keywords(source_archive: str, inner_path: str, text: str, timestamp: str, category: str) -> List[KeywordRow]:
    rows: List[KeywordRow] = []
    lower_text = text.lower()

    keyword_groups = [
        "ManagedSettings",
        "DMD",
        "Digital Health",
        "GameCenter",
        "gamecenter",
        "ScreenTime",
        "Family",
        "FindMy",
        "AppleAccount",
        "CloudServices",
        "CKKS",
        "PCS",
        "SOS",
        "FileProvider",
        "CloudDocs",
        "brctl",
        "WeChat",
        "ANECompilerService",
        "VisualIntelligence",
        "SiriSearchFeedback",
        "CommCenter",
        "MDMStatus",
        "LogWritingUsage",
        "LogRetirement",
        "saved 0",
        "file system out of space",
    ]

    for kw in keyword_groups:
        count = lower_text.count(kw.lower())
        if count:
            rows.append(
                KeywordRow(
                    source_archive=source_archive,
                    filename=Path(inner_path).name,
                    timestamp=timestamp,
                    category=category,
                    keyword=kw,
                    count=count,
                )
            )
    return rows


def extract_analytics_selected(source_archive: str, inner_path: str, text: str) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for line in text.splitlines()[1:]:
        s = line.strip().rstrip(",")
        if not s.startswith("{"):
            continue
        try:
            obj = json.loads(s)
        except Exception:
            continue
        if obj.get("name") in SELECTED_ANALYTICS_NAMES:
            rows.append(
                {
                    "source_archive": source_archive,
                    "filename": Path(inner_path).name,
                    "name": obj.get("name", ""),
                    "payload": json.dumps(obj, ensure_ascii=False, sort_keys=True),
                }
            )
    return rows


def extract_rtc_sfa_counts(source_archive: str, inner_path: str, text: str) -> List[Dict[str, Any]]:
    filename = Path(inner_path).name
    rows: List[Dict[str, Any]] = []

    patterns = {
        "eventName": r'"eventName"\s*:\s*"([^"]+)"',
        "processName": r'"processName"\s*:\s*"([^"]+)"',
        "name": r'"name"\s*:\s*"([^"]+)"',
        "subsystem": r'"subsystem"\s*:\s*"([^"]+)"',
    }

    for label, pat in patterns.items():
        c = Counter(re.findall(pat, text))
        for value, count in c.most_common(50):
            rows.append(
                {
                    "source_archive": source_archive,
                    "filename": filename,
                    "field": label,
                    "value": value,
                    "count": count,
                }
            )

    return rows


def process_text_artifact(
    source_archive: str,
    inner_path: str,
    data: bytes,
    all_files: List[FileRow],
    diskwrites: List[DiskWriteRow],
    stackshots: List[StackshotRow],
    keywords: List[KeywordRow],
    analytics_selected: List[Dict[str, Any]],
    rtc_sfa_counts: List[Dict[str, Any]],
) -> None:
    filename = Path(inner_path).name
    category = classify_file(filename, inner_path)

    if data == b"__SYSDIAGNOSE_ARCHIVE_PLACEHOLDER__":
        all_files.append(
            FileRow(
                source_archive=source_archive,
                inner_path=inner_path,
                filename=filename,
                category=category,
                timestamp="",
                bug_type="",
                app_name="",
                process_name="",
                size_bytes=0,
                sha256_16="sysdiagnose",
            )
        )
        return

    text = safe_decode(data)
    header = parse_json_header(text)

    timestamp = get_header_field(header, "timestamp")
    bug_type = get_header_field(header, "bug_type")
    app_name = get_header_field(header, "app_name", "name")
    process_name = get_header_field(header, "procName", "processName")

    all_files.append(
        FileRow(
            source_archive=source_archive,
            inner_path=inner_path,
            filename=filename,
            category=category,
            timestamp=timestamp,
            bug_type=bug_type,
            app_name=app_name,
            process_name=process_name,
            size_bytes=len(data),
            sha256_16=sha256_16(data),
        )
    )

    if category == "diskwrites_resource":
        diskwrites.append(parse_diskwrite(source_archive, inner_path, text, header))

    if category == "stackshot":
        row = parse_stackshot(source_archive, inner_path, text, header)
        if row:
            stackshots.append(row)

    if category == "Analytics":
        analytics_selected.extend(extract_analytics_selected(source_archive, inner_path, text))

    if category in {"RTCReporting", "SFA"}:
        rtc_sfa_counts.extend(extract_rtc_sfa_counts(source_archive, inner_path, text))

    keywords.extend(count_keywords(source_archive, inner_path, text, timestamp, category))


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


def write_summary(path: Path, files: List[FileRow], diskwrites: List[DiskWriteRow], stackshots: List[StackshotRow]) -> None:
    category_count = Counter(r.category for r in files)
    bug_count = Counter(r.bug_type for r in files if r.bug_type)
    source_count = Counter(r.source_archive for r in files)

    lines = []
    lines.append("# Anchor Event Summary")
    lines.append("")
    lines.append("## Source count")
    for k, v in source_count.most_common():
        lines.append(f"- `{k}`: {v}")
    lines.append("")
    lines.append("## Category count")
    for k, v in category_count.most_common():
        lines.append(f"- `{k}`: {v}")
    lines.append("")
    lines.append("## Bug type count")
    for k, v in bug_count.most_common():
        lines.append(f"- `{k}`: {v}")
    lines.append("")
    lines.append("## Disk-write events")
    for r in diskwrites:
        lines.append(f"- `{r.timestamp}` `{r.filename}` writes=`{r.writes}` free=`{r.free_disk_space}` path=`{r.process_or_path}`")
    lines.append("")
    lines.append("## Stackshot pressure highlights")
    for r in stackshots:
        lines.append(
            f"- `{r.timestamp}` `{r.filename}` free={r.free_pages} "
            f"purgeable={r.purgeable_pages} pagesWanted={r.pages_wanted} "
            f"processes={r.process_count}"
        )

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

    files: List[FileRow] = []
    diskwrites: List[DiskWriteRow] = []
    stackshots: List[StackshotRow] = []
    keywords: List[KeywordRow] = []
    analytics_selected: List[Dict[str, Any]] = []
    rtc_sfa_counts: List[Dict[str, Any]] = []

    for zip_path in sorted(in_dir.rglob("*.zip")):
        source_archive = str(zip_path.relative_to(in_dir))
        for inner_path, data in iter_zip_text_files(zip_path):
            process_text_artifact(
                source_archive,
                inner_path,
                data,
                files,
                diskwrites,
                stackshots,
                keywords,
                analytics_selected,
                rtc_sfa_counts,
            )

    for loose_path, data in iter_loose_text_files(in_dir):
        source_archive = "loose_files"
        inner_path = str(loose_path.relative_to(in_dir))
        process_text_artifact(
            source_archive,
            inner_path,
            data,
            files,
            diskwrites,
            stackshots,
            keywords,
            analytics_selected,
            rtc_sfa_counts,
        )

    write_csv(out_dir / "file_inventory.csv", files, list(FileRow.__dataclass_fields__.keys()))
    write_json(out_dir / "file_inventory.json", files)

    write_csv(out_dir / "diskwrites.csv", diskwrites, list(DiskWriteRow.__dataclass_fields__.keys()))
    write_json(out_dir / "diskwrites.json", diskwrites)

    write_csv(out_dir / "stackshots.csv", stackshots, list(StackshotRow.__dataclass_fields__.keys()))
    write_json(out_dir / "stackshots.json", stackshots)

    write_csv(out_dir / "keyword_counts.csv", keywords, list(KeywordRow.__dataclass_fields__.keys()))
    write_json(out_dir / "keyword_counts.json", keywords)

    if analytics_selected:
        write_csv(out_dir / "analytics_selected.csv", analytics_selected, ["source_archive", "filename", "name", "payload"])
        write_json(out_dir / "analytics_selected.json", analytics_selected)

    if rtc_sfa_counts:
        write_csv(out_dir / "rtc_sfa_counts.csv", rtc_sfa_counts, ["source_archive", "filename", "field", "value", "count"])
        write_json(out_dir / "rtc_sfa_counts.json", rtc_sfa_counts)

    write_summary(out_dir / "summary.md", files, diskwrites, stackshots)

    print(f"[OK] wrote output to: {out_dir}")
    print(f"[OK] files: {len(files)}")
    print(f"[OK] diskwrites: {len(diskwrites)}")
    print(f"[OK] stackshots: {len(stackshots)}")
    print(f"[OK] keyword rows: {len(keywords)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
