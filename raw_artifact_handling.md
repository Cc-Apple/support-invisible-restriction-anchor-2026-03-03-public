# Raw Artifact Handling Policy

## Purpose

This document defines how raw logs, sysdiagnose archives, and other sensitive artifacts should be handled for the 2026-03-03 support-invisible restriction anchor.

This public repository does **not** contain raw evidence.

It contains only public summaries, indexes, SHA256 references, review questions, and analysis scripts.

## Public repository boundary

Raw artifacts are not included in this public repository.

The following are excluded:

```text
raw iOS logs
raw sysdiagnose archives
Manifest.db files
iMazing backup folders
Apple ID values
account traces
device identifiers
BSSID / Wi-Fi identifiers
banking records
OTP records
private screenshots
friend or third-party identifiers
full physical-location records
```

## Safe to keep in this public repository

The following are suitable for public preliminary review:

```text
README.md
technical summaries
machine-readable summaries
SHA256 references
artifact indexes
referenced log titles
forensic review questions
non-attribution statement
extraction / analysis scripts
raw artifact handling notes
```

## Referenced raw artifacts for this case

The 2026-03-03 anchor is associated with the following preserved raw artifacts.

These files are **not included** in this public repository.

### Primary iOS log archive

```text
15G-2026-03-03.zip
```

Role:

```text
Primary same-day iOS log archive for the 2026-03-03 support-invisible restriction anchor.
```

Referenced contents include:

```text
Grab-2026-03-03-162129.ips
ospredictiond.cpu_resource-2026-03-03-163418.ips
signpost_reporter.cpu_resource-2026-03-03-164816.ips
fileproviderd.diskwrites_resource
xp_amp_app_usage_dnu
Analytics-2026-03-04-070009.ips.ca.synced
```

### Referenced sysdiagnose archives

```text
sysdiagnose_2026.03.03_11-53-34+0700_iPhone-OS_iPhone_22F76.tar.gz
sysdiagnose_2026.03.03_12-14-27+0700_iPhone-OS_iPhone_22F76.tar.gz
sysdiagnose_2026.03.03_20-09-49+0700_iPhone-OS_iPhone_22F76.tar.gz
sysdiagnose_2026.03.03_20-51-10+0700_iPhone-OS_iPhone_22F76.tar.gz
sysdiagnose_2026.03.03_21-34-04+0700_iPhone-OS_iPhone_22F76.tar.gz
```

## SHA256 handling

Raw artifacts should be identified by SHA256.

The SHA256 values are listed in the public artifact index and machine-readable summary.

A reviewer should verify SHA256 before relying on any raw artifact provided later.

## Recommended transfer process

If a qualified forensic reviewer requests raw artifacts, the transfer method should be agreed first.

Preferred options:

```text
secure upload portal provided by the reviewer
encrypted archive with password shared through a separate channel
NDA / evidence-handling agreement
formal chain-of-custody process
controlled physical review if device-level examination is required
```

Avoid casual public sharing of raw sysdiagnose archives or raw iOS logs.

## External storage note

Large raw diagnostic archives are preserved separately.

They may be stored offline, in restricted storage, or transferred through a forensic provider’s secure upload process.

Public GitHub is used only for the summary package, not for raw evidence distribution.

## Boundary

Raw artifacts are preserved for technical validation.

They do not by themselves establish:

```text
malware
payload
C2
exploit chain
APT attribution
state attribution
Apple attribution
criminal attribution
attacker identity
MDM enrollment
```

This handling policy exists to preserve reviewability while avoiding unnecessary public exposure of sensitive raw evidence.
