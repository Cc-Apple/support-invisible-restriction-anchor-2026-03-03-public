import os
import json
import gzip
import tarfile
import zipfile
import hashlib
import plistlib
from pathlib import Path

INPUTS = [
"15G-2026-03-03.zip",
"sysdiagnose_2026.03.03_11-53-34+0700_iPhone-OS_iPhone_22F76.tar.gz",
"sysdiagnose_2026.03.03_12-14-27+0700_iPhone-OS_iPhone_22F76.tar.gz",
"sysdiagnose_2026.03.03_20-09-49+0700_iPhone-OS_iPhone_22F76.tar.gz",
"sysdiagnose_2026.03.03_20-51-10+0700_iPhone-OS_iPhone_22F76.tar.gz",
"sysdiagnose_2026.03.03_21-34-04+0700_iPhone-OS_iPhone_22F76.tar.gz",
]

TERMS = [
"managedsettings",
"screentime",
"familycontrols",
"restriction",
"restricted",
"signout",
"sign out",
"appleid",
"icloud",
"cloudkit",
"cloudservices",
"sfa",
"ckks",
"commcenter",
"baseband",
"telephonybaseband",
"plmn",
"mcc",
"mnc",
"carrier",
"findmy",
"findmylocated",
"mdm",
"supervised",
"profile",
"configuration",
"allowpairing",
"privacyproxy",
"fileprovider",
"needs-auth",
"domain hidden",
]

KEY_ZIP_NAMES = [
"Analytics-2026-03-04-070009",
"Grab-2026-03-03-162129",
"ospredictiond.cpu_resource-2026-03-03-163418",
"signpost_reporter.cpu_resource-2026-03-03-164816",
"fileproviderd.diskwrites_resource",
"xp_amp_app_usage_dnu",
]

KEY_MCSTATE_NAMES = [
"cloudconfigurationdetails",
"payloadmanifest",
"profiletruth",
"payloaddependency",
"clienttruth",
"usersettings",
"effectiveusersettings",
"publiceffectiveusersettings",
]

def sha256_file(path):
h = hashlib.sha256()
with open(path, "rb") as f:
for chunk in iter(lambda: f.read(1024 * 1024), b""):
h.update(chunk)
return h.hexdigest()

def sha256_bytes(data):
return hashlib.sha256(data).hexdigest()

def gzip_integrity(path):
try:
with gzip.open(path, "rb") as f:
while f.read(1024 * 1024):
pass
return "OK"
except Exception as e:
return f"ERROR: {type(e).**name**}: {e}"

def safe_decode(data):
return data.decode("utf-8", "replace")

def safe_plist(data):
try:
return plistlib.loads(data)
except Exception as e:
return {"_plist_parse_error": f"{type(e).**name**}: {e}"}

def count_terms(text):
low = text.lower()
return {term: low.count(term) for term in TERMS if low.count(term) > 0}

def scan_zip(path):
result = {
"file": os.path.basename(path),
"type": "zip",
"sha256": sha256_file(path),
"size": os.path.getsize(path),
"entries": [],
}

```
with zipfile.ZipFile(path) as z:
    for info in z.infolist():
        if info.is_dir():
            continue

        name = info.filename
        if not any(k in name for k in KEY_ZIP_NAMES):
            continue

        data = z.read(name)
        text = safe_decode(data)
        low = text.lower()

        result["entries"].append({
            "path": name,
            "size": len(data),
            "sha256": sha256_bytes(data),
            "term_counts": count_terms(text),
            "mdmstatus_false_hits": low.count('"mdmstatus":false'),
            "commcenter_hits": low.count("commcenter"),
            "baseband_hits": low.count("baseband"),
            "telephonybaseband_hits": low.count("telephonybaseband"),
            "mobifone_hits": low.count("mobifone"),
            "trial_hits": low.count("trial"),
            "parsec_hits": low.count("parsec"),
            "searchd_hits": low.count("searchd"),
            "deleted_hits": low.count("deleted"),
            "fileprovider_hits": low.count("fileprovider"),
            "findmy_hits": low.count("findmy"),
            "usageclientid_hits": low.count("usageclientid"),
        })

return result
```

def open_tar_best_effort(path):
try:
return tarfile.open(path, "r:gz"), "r:gz"
except Exception:
return tarfile.open(path, "r|gz"), "r|gz"

def is_relevant_mcstate(path_lower):
if "logs/mcstate/" not in path_lower:
return False
if not path_lower.endswith(".plist"):
return False
base = os.path.basename(path_lower)
if base.startswith("._"):
return False
return any(k in path_lower for k in KEY_MCSTATE_NAMES)

def scan_sysdiagnose(path):
result = {
"file": os.path.basename(path),
"type": "sysdiagnose_tar_gz",
"sha256": sha256_file(path),
"size": os.path.getsize(path),
"gzip_integrity": gzip_integrity(path),
"tar_mode": None,
"members_read": 0,
"managed_settings": [],
"mcstate": [],
"fileprovider": [],
"findmy_hits": 0,
"term_totals": {},
"read_errors": [],
}

```
totals = {}

try:
    tf, mode = open_tar_best_effort(path)
    result["tar_mode"] = mode

    with tf:
        for m in tf:
            result["members_read"] += 1

            if not m.isfile():
                continue

            try:
                extracted = tf.extractfile(m)
                if extracted is None:
                    continue
                data = extracted.read()
            except Exception as e:
                result["read_errors"].append({
                    "path": m.name,
                    "error": f"{type(e).__name__}: {e}",
                })
                continue

            name = m.name
            lname = name.lower()
            text = safe_decode(data)
            low = text.lower()

            for term, count in count_terms(text).items():
                totals[term] = totals.get(term, 0) + count

            result["findmy_hits"] += low.count("findmy") + low.count("findmylocated")

            if "logs/managedsettings/" in lname:
                entry = {
                    "path": name,
                    "size": len(data),
                }
                if lname.endswith(".plist"):
                    entry["plist"] = safe_plist(data)
                else:
                    entry["text_head"] = text[:1500]
                result["managed_settings"].append(entry)

            if is_relevant_mcstate(lname):
                result["mcstate"].append({
                    "path": name,
                    "size": len(data),
                    "plist": safe_plist(data),
                })

            if "fileprovider" in lname:
                if "clouddocs.iclouddrivefileprovider" in lname or "fileproviderd.diskwrites" in lname:
                    result["fileprovider"].append({
                        "path": name,
                        "size": len(data),
                        "needs_auth": "needs-auth" in low,
                        "domain_hidden": "domain hidden" in low,
                        "indexer_enabled": "indexer enabled" in low,
                        "text_head": text[:1500],
                    })

except Exception as e:
    result["archive_error"] = f"{type(e).__name__}: {e}"

result["term_totals"] = {k: v for k, v in sorted(totals.items()) if v}
return result
```

def summarize_findings(results):
summary = {
"managed_settings_seen": False,
"mcstate_seen": False,
"is_supervised_false_seen": False,
"post_setup_profile_false_seen": False,
"empty_payload_or_profile_structures_seen": False,
"mdmstatus_false_seen": False,
"fileprovider_context_seen": False,
"findmy_context_seen": False,
"partial_archives": [],
}

```
for r in results:
    if r.get("type") == "sysdiagnose_tar_gz":
        if r.get("managed_settings"):
            summary["managed_settings_seen"] = True
        if r.get("mcstate"):
            summary["mcstate_seen"] = True
        if r.get("findmy_hits", 0) > 0:
            summary["findmy_context_seen"] = True
        if r.get("fileprovider"):
            summary["fileprovider_context_seen"] = True
        if r.get("gzip_integrity") != "OK":
            summary["partial_archives"].append({
                "file": r.get("file"),
                "gzip_integrity": r.get("gzip_integrity"),
                "members_read": r.get("members_read"),
            })

        mc_json = json.dumps(r.get("mcstate", []), ensure_ascii=False).lower()

        if '"issupervised": false' in mc_json:
            summary["is_supervised_false_seen"] = True
        if '"postsetupprofilewasinstalled": false' in mc_json:
            summary["post_setup_profile_false_seen"] = True
        if '"orderedprofiles": []' in mc_json or '"hiddenprofiles": []' in mc_json:
            summary["empty_payload_or_profile_structures_seen"] = True
        if '"profiletruth": {}' in mc_json or '"payloaddependency": {}' in mc_json:
            summary["empty_payload_or_profile_structures_seen"] = True

    if r.get("type") == "zip":
        for e in r.get("entries", []):
            if e.get("mdmstatus_false_hits", 0) > 0:
                summary["mdmstatus_false_seen"] = True
            if e.get("fileprovider_hits", 0) > 0:
                summary["fileprovider_context_seen"] = True
            if e.get("findmy_hits", 0) > 0:
                summary["findmy_context_seen"] = True

return summary
```

def main():
results = []

```
for name in INPUTS:
    p = Path(name)
    if not p.exists():
        results.append({
            "file": name,
            "error": "not found in current directory",
        })
        continue

    if name.endswith(".zip"):
        results.append(scan_zip(str(p)))
    elif name.endswith(".tar.gz"):
        results.append(scan_sysdiagnose(str(p)))
    else:
        results.append({
            "file": name,
            "error": "unsupported file type",
        })

output = {
    "case": "2026-03-03 Support-invisible restriction anchor",
    "purpose": "Best-effort reproducibility scan for ManagedSettings, MCState, MDMStatus:false, FileProvider, and auxiliary Find My context.",
    "safety": "This script reads files only and writes no output unless redirected by the user.",
    "inputs_expected_in_current_directory": INPUTS,
    "summary": summarize_findings(results),
    "results": results,
}

print(json.dumps(output, ensure_ascii=False, indent=2))
```

if **name** == "**main**":
main()
