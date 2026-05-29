# SHA256 Reference Index

## Purpose

This file provides a public SHA256 reference index structure for preserved artifacts.

Raw artifacts are not included in this public repository.

SHA256 values should be added only when they have been computed from preserved original artifacts.

---

## Scope

This index is intended for:

* local log ZIP archives
* sysdiagnose archives
* private screenshot files
* private video files
* extracted artifact summaries
* script outputs
* evidence packages prepared for qualified review

---

## Important rule

Do not invent SHA256 values.

If a SHA256 value has not been computed yet, use:

`pending`

If a file is preserved privately but not public, use:

`private-preserved`

If a file is not available, use:

`not-available`

---

## 2026-03-03 references

### Local log package

| Artifact   |            Status |  SHA256 |
| ---------- | ----------------: | ------: |
| `Logs.zip` | private-preserved | pending |

---

### Sysdiagnose archives

| Artifact                                                             |            Status |  SHA256 |
| -------------------------------------------------------------------- | ----------------: | ------: |
| `sysdiagnose_2026.03.03_11-53-34+0700_iPhone-OS_iPhone_22F76.tar.gz` | private-preserved | pending |
| `sysdiagnose_2026.03.03_12-14-27+0700_iPhone-OS_iPhone_22F76.tar.gz` | private-preserved | pending |
| `sysdiagnose_2026.03.03_20-09-49+0700_iPhone-OS_iPhone_22F76.tar.gz` | private-preserved | pending |
| `sysdiagnose_2026.03.03_20-51-10+0700_iPhone-OS_iPhone_22F76.tar.gz` | private-preserved | pending |
| `sysdiagnose_2026.03.03_21-34-04+0700_iPhone-OS_iPhone_22F76.tar.gz` | private-preserved | pending |

---

## 2026-03-04 references

### Local log package

| Artifact             |            Status |  SHA256 |
| -------------------- | ----------------: | ------: |
| `15G-2026-03-04.zip` | private-preserved | pending |

---

### Sysdiagnose archive

| Artifact                                                             |            Status |  SHA256 |
| -------------------------------------------------------------------- | ----------------: | ------: |
| `sysdiagnose_2026.03.04_05-13-59+0700_iPhone-OS_iPhone_22F76.tar.gz` | private-preserved | pending |

---

### Private screenshot / video evidence

| Private evidence                                                        |            Status |  SHA256 |
| ----------------------------------------------------------------------- | ----------------: | ------: |
| `2026-03-04 04:20 UTC+7 - Apple Pay stopped notification`               | private-preserved | pending |
| `2026-03-04 04:21 UTC+7 - Lost Mode enabled notification`               | private-preserved | pending |
| `2026-03-04 04:20-04:50 UTC+7 - screenshot/video evidence window`       | private-preserved | pending |
| `2026-03-04 04:43 UTC+7 - Game Center UI screenshot`                    | private-preserved | pending |
| `2026-03-04 23:13 UTC+7 - ChatGPT physical-sensation report screenshot` | private-preserved | pending |

---

## 2026-03-05 references

### Local log package

| Artifact             |            Status |  SHA256 |
| -------------------- | ----------------: | ------: |
| `15G-2026-03-05.zip` | private-preserved | pending |

---

### Sysdiagnose archives

| Artifact                                                             |            Status |  SHA256 |
| -------------------------------------------------------------------- | ----------------: | ------: |
| `sysdiagnose_2026.03.05_04-02-35+0700_iPhone-OS_iPhone_22F76.tar.gz` | private-preserved | pending |
| `sysdiagnose_2026.03.05_04-14-45+0700_iPhone-OS_iPhone_22F76.tar.gz` | private-preserved | pending |
| `sysdiagnose_2026.03.05_05-13-59+0700_iPhone-OS_iPhone_22F76.tar.gz` | private-preserved | pending |
| `sysdiagnose_2026.03.05_08-20-59+0700_iPhone-OS_iPhone_22F76.tar.gz` | private-preserved | pending |
| `sysdiagnose_2026.03.05_18-11-13+0700_iPhone-OS_iPhone_22F76.tar.gz` | private-preserved | pending |
| `sysdiagnose_2026.03.05_21-22-25+0700_iPhone-OS_iPhone_22F76.tar.gz` | private-preserved | pending |

---

### Private screenshot / video / support evidence

| Private evidence                                                             |            Status |  SHA256 |
| ---------------------------------------------------------------------------- | ----------------: | ------: |
| `2026-03-05 05:11 UTC+7 - Family Sharing screenshot`                         | private-preserved | pending |
| `2026-03-05 09:50 UTC+7 - Contacts / phone-related screenshot`               | private-preserved | pending |
| `2026-03-05 11:08 UTC+7 - Find My screenshot`                                | private-preserved | pending |
| `2026-03-05 11:10-11:31 UTC+7 - Apple Support interaction records`           | private-preserved | pending |
| `2026-03-05 18:11 UTC+7 - Screen Time restriction screenshot`                | private-preserved | pending |
| `2026-03-05 18:12 UTC+7 - Screen Time / Apple ID sign-out restriction video` | private-preserved | pending |

---

## Recommended SHA256 command

For local verification on macOS or Linux:

```bash
shasum -a 256 "FILE_NAME"
```

For Windows PowerShell:

```powershell
Get-FileHash "FILE_NAME" -Algorithm SHA256
```

For Python:

```python
from pathlib import Path
import hashlib

path = Path("FILE_NAME")
h = hashlib.sha256()
with path.open("rb") as f:
    for chunk in iter(lambda: f.read(1024 * 1024), b""):
        h.update(chunk)
print(h.hexdigest())
```

---

## Reviewer use

A qualified reviewer may use this index to:

* confirm artifact identity
* detect accidental file replacement
* verify private evidence packages
* compare analysis outputs against preserved originals
* request only the specific private artifacts needed for review

---

## Boundary

This SHA256 index does not include raw artifact contents.

It does not prove:

* malware
* actor attribution
* Evil Twin / Rogue AP use
* malicious profile injection
* classic MDM enrollment
* Apple-side causation

It only defines the verification structure for preserved artifacts.
