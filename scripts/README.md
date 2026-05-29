# Scripts

## Purpose

This directory contains reproducibility scripts for the public technical review package.

The scripts are intended to help qualified reviewers reproduce the public summaries from preserved private artifacts.

Raw artifacts are not included in this repository.

---

## Script list

### `analyze_anchor_events.py`

Purpose:

* scan preserved local log ZIP files
* summarize event categories
* extract timeline rows
* identify stackshot memory pressure
* summarize disk-write resource records
* summarize selected Analytics / RTCReporting / SFA patterns

Primary use:

* 2026-03-03
* 2026-03-04
* 2026-03-05

---

### `extract_mcsettings_events.py`

Purpose:

* extract MCState / ManagedSettings / MCSettingsEvents records from sysdiagnose archives
* summarize visible management state
* extract Safari restriction changes
* extract DMD / Digital Health recomputation
* extract Game Center-related restriction paths
* compare EffectiveUserSettings values

Primary use:

* 2026-03-03 baseline
* 2026-03-04 Game Center baseline
* 2026-03-05 ManagedSettings / DMD recomputation window

---

### `compute_sha256_manifest.py`

Purpose:

* compute SHA256 hashes for preserved private artifacts
* generate a machine-readable manifest
* help fill `05_evidence_index/sha256_reference_index.md`

Primary use:

* local log ZIP archives
* sysdiagnose archives
* private screenshot/video files
* extracted summary outputs

---

## Public / private boundary

These scripts are public.

The raw artifacts they analyze are private.

Do not commit:

* raw iOS logs
* raw sysdiagnose archives
* raw screenshots
* raw videos
* Apple Support records
* Apple ID information
* phone numbers
* precise location data
* BSSID / SSID lists
* device identifiers
* private account data

---

## Expected input structure

The scripts assume a local private working directory, for example:

```text
private_artifacts/
├─ 2026-03-03/
│  ├─ Logs.zip
│  └─ sysdiagnose_*.tar.gz
├─ 2026-03-04/
│  ├─ 15G-2026-03-04.zip
│  └─ sysdiagnose_*.tar.gz
└─ 2026-03-05/
   ├─ 15G-2026-03-05.zip
   └─ sysdiagnose_*.tar.gz
```

This directory is only an example.

It should not be committed.

---

## Expected output structure

Recommended local output directory:

```text
review_output/
├─ anchor_events/
├─ mcsettings_events/
└─ sha256_manifest/
```

Output files may include:

* CSV summaries
* JSON summaries
* YAML summaries
* text reports

Reviewers should redact outputs before publishing if they contain private values.

---

## Running the scripts

Example:

```bash
python analyze_anchor_events.py --input private_artifacts --output review_output/anchor_events
```

```bash
python extract_mcsettings_events.py --input private_artifacts --output review_output/mcsettings_events
```

```bash
python compute_sha256_manifest.py --input private_artifacts --output review_output/sha256_manifest
```

---

## Dependency policy

The scripts are intended to use only Python standard library modules where possible.

Recommended Python version:

```text
Python 3.10+
```

---

## Safety boundary

These scripts are analysis tools only.

They do not:

* exploit devices
* connect to devices
* modify artifacts
* modify iCloud / Apple ID / Screen Time state
* install profiles
* perform network scanning
* perform credential capture
* perform decryption attacks

They only read local preserved artifacts and generate summaries.

---

## Review posture

Script output should be treated as derived analysis.

The original private artifacts remain the source of truth.

If a script output and a raw artifact disagree, reviewers should prioritize the raw artifact.
