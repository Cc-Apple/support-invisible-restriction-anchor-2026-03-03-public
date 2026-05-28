# Logs Directory

## Purpose

This directory is reserved for references to raw iOS log artifacts related to the 2026-03-03 support-invisible restriction anchor.

Raw iOS logs are **not included** in this public repository.

This directory exists only to document which raw log titles are referenced by the public review package.

## Public repository boundary

This public repository does not include:

```text
.ips raw log files
.ips.ca.synced raw log files
raw ZIP log archives
Manifest.db files
iMazing backup folders
BSSID values
Apple ID values
banking records
OTP records
private screenshots
```

The original raw logs are preserved separately.

They can be provided later through a secure upload method, NDA, or evidence-handling procedure if required by a qualified reviewer.

## Referenced raw log archive

```text
Archive:
  15G-2026-03-03.zip

SHA256:
  ef68c98c6336dd7f69403da3b87b0da22dfec3046096b44408c446b0d124d222

Role:
  Primary same-day iOS log archive for the 2026-03-03 support-invisible restriction anchor.
```

## Referenced log titles

```text
Grab-2026-03-03-162129.ips
ospredictiond.cpu_resource-2026-03-03-163418.ips
signpost_reporter.cpu_resource-2026-03-03-164816.ips
fileproviderd.diskwrites_resource
xp_amp_app_usage_dnu
Analytics-2026-03-04-070009.ips.ca.synced
```

## Review role

The referenced log titles support review of the following structure:

```text
same-day crash context
same-day CPU resource context
same-day FileProvider context
usage-state context
next-day Analytics showing MDMStatus:false
CommCenter / Baseband / TelephonyBaseband context in the next-day Analytics material
```

## Privacy warning

Raw iOS logs may contain sensitive information, including:

```text
device identifiers
account traces
app activity
network metadata
carrier / telecom context
timestamps
local paths
personal usage patterns
third-party identifiers
```

For this reason, raw logs are not published in this public repository.

## Evidence integrity

The referenced raw log archive is identified by SHA256.

A reviewer should verify the SHA256 value before relying on the raw artifact.

## Boundary

The referenced raw logs do not establish:

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

They are preserved for technical validation of the 2026-03-03 artifact correlation.
