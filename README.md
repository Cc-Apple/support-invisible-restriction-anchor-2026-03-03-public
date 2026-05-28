# Support Invisible Restriction Anchor - 2026-03-03 Public Package

## Status

Public preliminary technical review package.

This repository is intended for qualified digital forensics, incident response, mobile forensic, legal-technical, or security research review.

It is not a public accusation or attribution claim.

## Core observation

On 2026-03-03, the device internally labeled **15G** reportedly displayed a restriction preventing Apple ID sign-out in Settings.

According to the user's recollection and available contact-history records, Apple Support was contacted on the same date and reportedly could not confirm a visible Screen Time, Family Sharing, MDM, or supervised-management restriction from their side.

The same date contains preserved iOS logs and sysdiagnose artifacts showing a local restriction / policy-adjacent artifact structure.

## Public repository boundary

Raw iOS logs are **not included** in this public repository.

Raw sysdiagnose archives are **not included** in this public repository.

This public repository contains only:

* written technical summaries
* artifact indexes
* SHA256 references
* referenced log titles
* timeline summaries
* forensic review questions
* non-attribution statement
* raw artifact handling policy
* reproducibility / analysis script

The original raw logs and sysdiagnose archives are preserved separately and can be provided later through a secure upload method, NDA, or evidence-handling procedure if required by a qualified reviewer.

## Device

Internal label: **15G**

Physical class: **iPhone 12 mini class device**

Observed model identifier: **iPhone13,1**

Observed OS generation: **iPhone OS 18.5 / 22F76**

Important note: **15G is an internal Ghost / Apple ID lineage label. It does not mean the physical device is an iPhone 15 Pro.**

## Why this date matters

The 2026-03-03 evidence is important because the observed structure appears inconsistent with a simple visible MDM, supervised-device, or normal Family Sharing / Screen Time explanation.

The key issue is:

* Device side: Apple ID sign-out restriction reportedly visible.
* Apple Support side: visible Screen Time / Family Sharing / MDM / supervised-management restriction reportedly not confirmed.

This creates the following technical question:

Was this a normal local iOS policy edge case, a benign Screen Time / ManagedSettings state, an account / cloud / policy-adjacent restriction state, or a deeper control-layer anomaly requiring formal forensic review?

## Main artifact correlation

The same-day and next-day artifacts show the following structure:

* ManagedSettings / ScreenTime local stores
* com.apple.ScreenTime internal store activity
* com.apple.Preferences UserSafety store
* MCState showing `IsSupervised:false`
* MCState showing `PostSetupProfileWasInstalled:false`
* visible profile / payload manifest structures appearing empty
* next-day Analytics showing `MDMStatus:false`
* crash / CPU resource / FileProvider side effects on the same date
* Find My / findmylocated-adjacent artifacts as auxiliary context

## Timeline summary

* **2026-03-03 morning**: Apple Support contact records exist on the same date.
* **2026-03-03 11:53**: sysdiagnose captured. ManagedSettings / ScreenTime local store observed. MCState artifacts observed.
* **2026-03-03 12:14**: sysdiagnose captured. Similar ManagedSettings / MCState structure observed.
* **2026-03-03 16:21**: device log shows Grab crash. User recalls discussing the sign-out restriction with Apple Support on the same date.
* **2026-03-03 16:31-16:48**: ospredictiond CPU resource log and signpost_reporter CPU resource log. triald / deleted / searchd-adjacent context appears in related review.
* **2026-03-03 20:09**: sysdiagnose captured. Partial evidence due to gzip issue, but ManagedSettings context was still observed.
* **2026-03-03 20:51**: sysdiagnose captured. Partial evidence due to gzip issue, but ManagedSettings / MCState context was still observed.
* **2026-03-03 20:59**: fileproviderd diskwrites resource log.
* **2026-03-03 21:34**: sysdiagnose captured. ManagedSettings / MCState / FileProvider / Find My auxiliary context observed.
* **2026-03-04**: Analytics log contains `MDMStatus:false` with CommCenter / Baseband / TelephonyBaseband context.

## Referenced raw log titles

The raw log files listed below are **not included** in this public repository.

They are listed only to support later verification and evidence matching.

Primary archive:

* `15G-2026-03-03.zip`

Referenced contents:

* `Grab-2026-03-03-162129.ips`
* `ospredictiond.cpu_resource-2026-03-03-163418.ips`
* `signpost_reporter.cpu_resource-2026-03-03-164816.ips`
* `fileproviderd.diskwrites_resource`
* `xp_amp_app_usage_dnu`
* `Analytics-2026-03-04-070009.ips.ca.synced`

## Referenced sysdiagnose archives

The sysdiagnose archives listed below are **not included** in this public repository.

They are preserved separately.

* `sysdiagnose_2026.03.03_11-53-34+0700_iPhone-OS_iPhone_22F76.tar.gz`
* `sysdiagnose_2026.03.03_12-14-27+0700_iPhone-OS_iPhone_22F76.tar.gz`
* `sysdiagnose_2026.03.03_20-09-49+0700_iPhone-OS_iPhone_22F76.tar.gz`
* `sysdiagnose_2026.03.03_20-51-10+0700_iPhone-OS_iPhone_22F76.tar.gz`
* `sysdiagnose_2026.03.03_21-34-04+0700_iPhone-OS_iPhone_22F76.tar.gz`

## Key technical observations

### ManagedSettings / ScreenTime local store

Reviewed path:

* `logs/ManagedSettings/SettingRecords.plist`

Observed structure:

* `com.apple.ScreenTime`

  * `isInternal: true`
  * `store: SafariStore`
  * `active: true`

* `com.apple.Preferences`

  * `isInternal: true`
  * `store: UserSafety`
  * `active: false`
  * `syncToWatch: true`

### EffectiveSettings

Observed values include:

* `safari.denyPrivateBrowsing: false`
* `safari.denyHistoryClearing: false`

### MCState

Observed values include:

* `IsSupervised: false`
* `CloudConfigurationUIComplete: true`
* `ConfigurationSource: 0`
* `AllowPairing: true`
* `PostSetupProfileWasInstalled: false`

### Visible profile / payload structures

Observed structures include:

* `PayloadManifest`

  * `OrderedProfiles: []`
  * `HiddenProfiles: []`

* `ProfileTruth: {}`

* `PayloadDependency: {}`

### Next-day Analytics

Observed value:

* `MDMStatus:false`

## Working interpretation

The 2026-03-03 structure appears consistent with a support-invisible, device-local, or account / cloud / policy-adjacent restriction state.

This is a working technical hypothesis only.

It requires qualified forensic review.

## Important boundary

This repository does **not** establish:

* malware
* payload
* C2
* exploit chain
* APT attribution
* state attribution
* Apple attribution
* criminal attribution
* attacker identity
* MDM enrollment

## Main review question

Can the reported device-side Apple ID sign-out restriction and the observed ManagedSettings / ScreenTime / MCState / Analytics artifacts be explained by normal iOS behavior, or does the structure justify deeper mobile forensic review?

## Evidence handling

Raw artifacts are preserved separately.

If a qualified reviewer requests the raw files, the transfer method should be agreed first.

Preferred options:

* secure upload portal provided by the reviewer
* encrypted archive with password shared through a separate channel
* formal evidence-handling agreement
* NDA if required
* controlled physical review if device-level examination is required
