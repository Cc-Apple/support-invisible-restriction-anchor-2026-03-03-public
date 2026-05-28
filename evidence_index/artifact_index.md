# Artifact Index: 2026-03-03

## Purpose

This file lists the referenced artifacts for the 2026-03-03 support-invisible restriction anchor.

Raw iOS logs and raw sysdiagnose archives are not included in this public repository.

The purpose is to help a qualified forensic reviewer understand which original files exist, what role each file plays, and which files can be requested later through a secure evidence-transfer process.

## Primary device

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
Public repository boundary

The raw artifacts listed below are preserved separately and are not included here.

This public repository contains only:

artifact index
SHA256 references
timeline summaries
technical observations
review questions
handling policy
analysis script
non-attribution statement
Referenced primary iOS log archive
File:
  15G-2026-03-03.zip

SHA256:
  ef68c98c6336dd7f69403da3b87b0da22dfec3046096b44408c446b0d124d222

Role:
  Primary same-day iOS log archive.

Referenced contents:
  Grab-2026-03-03-162129.ips
  ospredictiond.cpu_resource-2026-03-03-163418.ips
  signpost_reporter.cpu_resource-2026-03-03-164816.ips
  fileproviderd.diskwrites_resource
  xp_amp_app_usage_dnu
  Analytics-2026-03-04-070009.ips.ca.synced

Key relevance:
  16:21 crash cluster
  CPU resource logs
  FileProvider context
  usage-state context
  next-day Analytics showing MDMStatus:false
Referenced sysdiagnose archives
1.
Filename:
  sysdiagnose_2026.03.03_11-53-34+0700_iPhone-OS_iPhone_22F76.tar.gz

SHA256:
  fb85aab16185671ffe1cfe8eb24b298e242e5d40d1a115367570f8784fc911a3

Gzip integrity:
  OK

Role:
  Primary sysdiagnose.

Observed relevance:
  ManagedSettings / ScreenTime local store
  MCState artifacts
  restriction / policy-adjacent context
2.
Filename:
  sysdiagnose_2026.03.03_12-14-27+0700_iPhone-OS_iPhone_22F76.tar.gz

SHA256:
  51e2df3d7fe3ceb67c2a292a9b1f60c296ed6baedbe264d98a520764784d5431

Gzip integrity:
  OK

Role:
  Primary sysdiagnose.

Observed relevance:
  ManagedSettings / ScreenTime local store repeated
  MCState structure repeated
3.
Filename:
  sysdiagnose_2026.03.03_20-09-49+0700_iPhone-OS_iPhone_22F76.tar.gz

SHA256:
  a87639996ef2a8f5a164fdde38bbb8b56ca711de4723f01b2514c83ce6f5ea52

Gzip integrity:
  CRC error observed

Role:
  Partial supporting sysdiagnose.

Observed relevance:
  ManagedSettings context observed despite archive integrity issue.

Handling note:
  Treat as partial supporting evidence.
  Preserve original file.
  Do not rely on this archive alone for final conclusions.
4.
Filename:
  sysdiagnose_2026.03.03_20-51-10+0700_iPhone-OS_iPhone_22F76.tar.gz

SHA256:
  4eaade44439216c4007701311f3384355b5bf7097bd665c3faa5d528d4e89df6

Gzip integrity:
  Decompression error observed

Role:
  Partial supporting sysdiagnose.

Observed relevance:
  ManagedSettings / MCState context observed during partial stream reading.

Handling note:
  Treat as partial supporting evidence.
  Preserve original file.
  Do not rely on this archive alone for final conclusions.
5.
Filename:
  sysdiagnose_2026.03.03_21-34-04+0700_iPhone-OS_iPhone_22F76.tar.gz

SHA256:
  97cdfa086688afad7c39ec98b3d0e0c5c14d2a3299d81a54d2108eefc7228b21

Gzip integrity:
  OK

Role:
  Primary late-day sysdiagnose.

Observed relevance:
  ManagedSettings / MCState / FileProvider / Find My auxiliary context
Key reviewed paths
ManagedSettings:
  logs/ManagedSettings/SettingRecords.plist
  logs/ManagedSettings/EffectiveSettings.plist
  logs/ManagedSettings/com.apple.ScreenTime/SafariStore.plist
  logs/ManagedSettings/com.apple.ScreenTime/clientEffectiveSettings.plist
  logs/ManagedSettings/com.apple.Preferences/UserSafety.plist
MCState:
  logs/MCState/Shared/CloudConfigurationDetails.plist
  logs/MCState/Shared/PayloadManifest.plist
  logs/MCState/Shared/ProfileTruth.plist
  logs/MCState/Shared/PayloadDependency.plist
  logs/MCState/Shared/ClientTruth.plist
iOS logs:
  Grab-2026-03-03-162129.ips
  ospredictiond.cpu_resource-2026-03-03-163418.ips
  signpost_reporter.cpu_resource-2026-03-03-164816.ips
  fileproviderd.diskwrites_resource
  Analytics-2026-03-04-070009.ips.ca.synced
Primary observations
ManagedSettings / ScreenTime local store exists
MCState shows IsSupervised:false
MCState shows PostSetupProfileWasInstalled:false
Visible profile / payload structures appear empty
Next-day Analytics shows MDMStatus:false
Same-day crash / CPU / FileProvider artifacts exist
Evidence handling note

The raw sysdiagnose archives and iOS log archives may contain sensitive device, account, app, network, carrier, location, and personal-usage information.

For this reason, raw artifacts are not published in this public repository.

They can be provided later through an agreed secure submission process if requested by a qualified reviewer.

Boundary

This index does not establish:

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

This file only identifies referenced evidence items and their review role.
