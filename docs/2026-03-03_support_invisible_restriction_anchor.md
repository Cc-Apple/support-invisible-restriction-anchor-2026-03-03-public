# 2026-03-03 Support-Invisible Restriction Anchor

## Summary

This document describes a specific artifact correlation observed on 2026-03-03 on the device internally labeled **15G**.

The key observation is:

```text
The device reportedly displayed an Apple ID sign-out restriction, while Apple Support reportedly could not confirm a visible Screen Time, Family Sharing, MDM, or supervised-management restriction from their side.
```

This does not prove compromise by itself.

However, the same date contains preserved iOS log and sysdiagnose artifact references that make this date important for qualified forensic review.

Raw iOS logs and raw sysdiagnose archives are not included in this public repository.

## Device context

```text
Internal label:
  15G

Physical class:
  iPhone 12 mini class device

Observed model identifier:
  iPhone13,1

Observed OS generation:
  iPhone OS 18.5 / 22F76

Important note:
  The label 15G is an internal Ghost / Apple ID lineage label.
  It does not mean the physical device is an iPhone 15 Pro.
```

## Why this date matters

A normal explanation would usually involve one of the following:

```text
visible Screen Time restriction
Family Sharing / parental control
MDM enrollment
supervised device state
installed configuration profile
known local iOS policy state
```

The reviewed artifacts instead show a more ambiguous structure:

```text
ManagedSettings / ScreenTime local stores exist
MCState shows IsSupervised:false
MCState shows PostSetupProfileWasInstalled:false
visible payload / profile structures appear empty
next-day Analytics shows MDMStatus:false
```

This creates a technical question:

```text
Can the device-side restriction be explained by normal local iOS policy behavior,
or does it represent a support-invisible account / cloud / policy-adjacent restriction state?
```

## Timeline

```text
2026-03-03 morning:
  Apple Support contact records exist on the same date.

2026-03-03 11:53:
  sysdiagnose captured.
  ManagedSettings / ScreenTime local store observed.
  MCState artifacts observed.

2026-03-03 12:14:
  sysdiagnose captured.
  Similar ManagedSettings / MCState structure observed.

2026-03-03 16:21:
  Device log shows Grab crash.
  The user recalls discussing the sign-out restriction with Apple Support on the same date.

2026-03-03 16:31-16:48:
  ospredictiond CPU resource log.
  signpost_reporter CPU resource log.
  triald / deleted / searchd-adjacent context appears in related review.

2026-03-03 20:09:
  sysdiagnose captured.
  Partial evidence due to gzip issue.
  ManagedSettings context was still observed.

2026-03-03 20:51:
  sysdiagnose captured.
  Partial evidence due to gzip issue.
  ManagedSettings / MCState context was still observed.

2026-03-03 20:59:
  fileproviderd diskwrites resource log.

2026-03-03 21:34:
  sysdiagnose captured.
  ManagedSettings / MCState / FileProvider / Find My auxiliary context observed.

2026-03-04:
  Analytics log contains MDMStatus:false with CommCenter / Baseband / TelephonyBaseband context.
```

## Referenced raw log archive

The raw archive listed below is **not included** in this public repository.

```text
Archive:
  15G-2026-03-03.zip

SHA256:
  ef68c98c6336dd7f69403da3b87b0da22dfec3046096b44408c446b0d124d222

Referenced contents:
  Grab-2026-03-03-162129.ips
  ospredictiond.cpu_resource-2026-03-03-163418.ips
  signpost_reporter.cpu_resource-2026-03-03-164816.ips
  fileproviderd.diskwrites_resource
  xp_amp_app_usage_dnu
  Analytics-2026-03-04-070009.ips.ca.synced
```

## Referenced sysdiagnose archives

The raw sysdiagnose archives listed below are **not included** in this public repository.

```text
sysdiagnose_2026.03.03_11-53-34+0700_iPhone-OS_iPhone_22F76.tar.gz
sysdiagnose_2026.03.03_12-14-27+0700_iPhone-OS_iPhone_22F76.tar.gz
sysdiagnose_2026.03.03_20-09-49+0700_iPhone-OS_iPhone_22F76.tar.gz
sysdiagnose_2026.03.03_20-51-10+0700_iPhone-OS_iPhone_22F76.tar.gz
sysdiagnose_2026.03.03_21-34-04+0700_iPhone-OS_iPhone_22F76.tar.gz
```

## ManagedSettings / ScreenTime observations

Repeated sysdiagnose artifacts include:

```text
logs/ManagedSettings/SettingRecords.plist
```

Observed structure:

```text
com.apple.ScreenTime:
  isInternal: true
  store: SafariStore
  active: true

com.apple.Preferences:
  isInternal: true
  store: UserSafety
  active: false
  syncToWatch: true
```

## EffectiveSettings observations

Observed values include:

```text
safari.denyPrivateBrowsing: false
safari.denyHistoryClearing: false
```

This suggests that the observed ManagedSettings state was not simply a visible Safari restriction.

## MCState observations

Observed values include:

```text
IsSupervised: false
CloudConfigurationUIComplete: true
ConfigurationSource: 0
AllowPairing: true
PostSetupProfileWasInstalled: false
```

Related visible profile / payload structures appeared empty in the reviewed artifacts:

```text
PayloadManifest:
  OrderedProfiles: []
  HiddenProfiles: []

ProfileTruth:
  {}

PayloadDependency:
  {}
```

## Next-day Analytics

The next-day Analytics log contains:

```text
MDMStatus:false
```

The same broader context contains:

```text
CommCenter
Baseband
TelephonyBaseband
carrier-related artifacts
```

## Auxiliary context

The same date also contains auxiliary artifacts involving:

```text
crash / CPU resource logs
FileProvider state
Find My / findmylocated references
triald / deleted / searchd-adjacent context
```

These auxiliary artifacts are not used as standalone proof.

They are preserved as timing context around the support-invisible restriction anchor.

## Working interpretation

The 2026-03-03 structure appears consistent with a support-invisible, device-local, or account / cloud / policy-adjacent restriction state.

It strengthens the broader working hypothesis:

```text
MDM=false / supervised=false / visible-profile absent,
yet restriction-management-adjacent behavior appears at the device artifact level.
```

This remains a working technical hypothesis requiring qualified forensic review.

## Boundary

This document does not establish:

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

It documents a structured artifact correlation for expert review.

## Evidence boundary

Raw iOS logs and raw sysdiagnose archives are not included in this public repository.

The original raw evidence is preserved separately and can be provided later through a secure upload method, NDA, or evidence-handling procedure if required by a qualified reviewer.
