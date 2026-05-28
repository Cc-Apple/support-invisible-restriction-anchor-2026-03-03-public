# Extracted Artifacts Directory

## Purpose

This directory is reserved for notes about selected extracted artifacts from the 2026-03-03 sysdiagnose and iOS log files.

Extracted artifacts are **not included** in this public repository.

This directory exists only to document which extracted paths were reviewed and which artifacts may be requested later by a qualified forensic reviewer.

## Public repository boundary

This public repository does not include:

```text
raw iOS logs
raw sysdiagnose archives
extracted plist files
extracted databases
extracted text artifacts
private screenshots
device identifiers
account identifiers
BSSID values
banking or OTP records
```

The original raw files and extracted artifacts are preserved separately.

They can be provided later through a secure upload method, NDA, or evidence-handling procedure if required by a qualified reviewer.

## Relevant extracted artifact paths

The following paths were identified as relevant during review.

They refer to paths inside preserved raw sysdiagnose archives or raw iOS log archives.

### ManagedSettings

```text
ManagedSettings/SettingRecords.plist
ManagedSettings/EffectiveSettings.plist
ManagedSettings/com.apple.ScreenTime/SafariStore.plist
ManagedSettings/com.apple.ScreenTime/clientEffectiveSettings.plist
ManagedSettings/com.apple.Preferences/UserSafety.plist
```

### MCState

```text
MCState/CloudConfigurationDetails.plist
MCState/PayloadManifest.plist
MCState/ProfileTruth.plist
MCState/PayloadDependency.plist
MCState/ClientTruth.plist
```

### iOS log titles

```text
Analytics-2026-03-04-070009.ips.ca.synced
Grab-2026-03-03-162129.ips
ospredictiond.cpu_resource-2026-03-03-163418.ips
signpost_reporter.cpu_resource-2026-03-03-164816.ips
fileproviderd.diskwrites_resource
```

## Review role

These extracted artifact references support review of the following structure:

```text
ManagedSettings / ScreenTime local store
MCState configuration state
visible profile / payload structure
next-day Analytics MDMStatus:false
same-day crash / CPU / FileProvider context
```

## Handling note

Extracted artifacts are not a substitute for the original raw files.

The raw files remain the evidence source.

Any extracted artifact should be traceable back to the original preserved raw file and SHA256 reference.

## Boundary

This directory does not establish:

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

This directory only documents referenced extracted artifact paths for later review.
