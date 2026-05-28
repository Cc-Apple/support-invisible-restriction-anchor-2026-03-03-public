# Sysdiagnose Directory

## Purpose

This directory is reserved for references to sysdiagnose archives related to the 2026-03-03 support-invisible restriction anchor.

Raw sysdiagnose archives are **not included** in this public repository.

This directory exists only to document which sysdiagnose archives are referenced by the public review package.

## Public repository boundary

This public repository does not include:

```text
raw sysdiagnose archives
extracted sysdiagnose files
diagnostic databases
device identifiers
Apple account traces
networking metadata
Wi-Fi / Bluetooth context
carrier / baseband / telecom context
local paths
usage and process history
private screenshots
```

The original sysdiagnose archives are preserved separately.

They can be provided later through a secure upload method, NDA, or evidence-handling procedure if required by a qualified reviewer.

## Referenced sysdiagnose archives

```text
1.
Filename:
  sysdiagnose_2026.03.03_11-53-34+0700_iPhone-OS_iPhone_22F76.tar.gz

SHA256:
  fb85aab16185671ffe1cfe8eb24b298e242e5d40d1a115367570f8784fc911a3

Integrity:
  OK

Role:
  Primary sysdiagnose.
```

```text
2.
Filename:
  sysdiagnose_2026.03.03_12-14-27+0700_iPhone-OS_iPhone_22F76.tar.gz

SHA256:
  51e2df3d7fe3ceb67c2a292a9b1f60c296ed6baedbe264d98a520764784d5431

Integrity:
  OK

Role:
  Primary sysdiagnose.
```

```text
3.
Filename:
  sysdiagnose_2026.03.03_20-09-49+0700_iPhone-OS_iPhone_22F76.tar.gz

SHA256:
  a87639996ef2a8f5a164fdde38bbb8b56ca711de4723f01b2514c83ce6f5ea52

Integrity:
  CRC error observed

Role:
  Partial supporting sysdiagnose.
```

```text
4.
Filename:
  sysdiagnose_2026.03.03_20-51-10+0700_iPhone-OS_iPhone_22F76.tar.gz

SHA256:
  4eaade44439216c4007701311f3384355b5bf7097bd665c3faa5d528d4e89df6

Integrity:
  Decompression error observed

Role:
  Partial supporting sysdiagnose.
```

```text
5.
Filename:
  sysdiagnose_2026.03.03_21-34-04+0700_iPhone-OS_iPhone_22F76.tar.gz

SHA256:
  97cdfa086688afad7c39ec98b3d0e0c5c14d2a3299d81a54d2108eefc7228b21

Integrity:
  OK

Role:
  Primary late-day sysdiagnose.
```

## Key reviewed paths

The following paths were identified as relevant during review.

These paths refer to locations inside the preserved raw sysdiagnose archives.

```text
ManagedSettings:
  logs/ManagedSettings/SettingRecords.plist
  logs/ManagedSettings/EffectiveSettings.plist
  logs/ManagedSettings/com.apple.ScreenTime/SafariStore.plist
  logs/ManagedSettings/com.apple.ScreenTime/clientEffectiveSettings.plist
  logs/ManagedSettings/com.apple.Preferences/UserSafety.plist
```

```text
MCState:
  logs/MCState/Shared/CloudConfigurationDetails.plist
  logs/MCState/Shared/PayloadManifest.plist
  logs/MCState/Shared/ProfileTruth.plist
  logs/MCState/Shared/PayloadDependency.plist
  logs/MCState/Shared/ClientTruth.plist
```

## Review role

The referenced sysdiagnose archives support review of the following structure:

```text
ManagedSettings / ScreenTime local store
MCState configuration state
IsSupervised:false
PostSetupProfileWasInstalled:false
visible profile / payload structures appearing empty
FileProvider context
Find My / findmylocated auxiliary context
```

## Integrity note

Three sysdiagnose archives are treated as primary readable archives.

Two sysdiagnose archives are treated only as partial supporting evidence because integrity or decompression issues were observed.

Partial archives should not be used alone for final conclusions.

## Privacy warning

Raw sysdiagnose archives may contain highly sensitive information.

For this reason, raw sysdiagnose archives are not published in this public repository.

## Boundary

The referenced sysdiagnose archives do not establish:

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
