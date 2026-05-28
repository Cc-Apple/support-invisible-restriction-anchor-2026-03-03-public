# Forensic Review Questions

## Purpose

This document lists the questions that should be reviewed by a qualified DFIR / mobile forensic specialist.

The purpose is not attribution.

The purpose is to determine whether the 2026-03-03 artifact correlation is technically meaningful and whether deeper forensic review is justified.

## Primary review question

Can normal iOS / Apple ID / Screen Time / Family Sharing / MDM / supervised-device behavior explain the following structure?

```text
Device-side Apple ID sign-out restriction reportedly visible to the user
Apple Support reportedly unable to confirm a visible restriction from their side
ManagedSettings / ScreenTime local stores present
MCState showing IsSupervised:false
MCState showing PostSetupProfileWasInstalled:false
Visible profile / payload structures appearing empty
Next-day Analytics showing MDMStatus:false
Same-day crash / CPU / FileProvider side effects
Question group 1: Apple Support visibility
What restriction states can Apple Support normally confirm from their side?

Can Apple Support see all Screen Time / Family Sharing restriction states?

Can a device show Apple ID sign-out restriction while Apple Support cannot see the cause?

Are there known benign cases where Apple Support cannot confirm a restriction that is visible on-device?

What Apple-side logs, support case records, or support-side notes would best confirm the support interaction?
Question group 2: Screen Time / ManagedSettings
What does logs/ManagedSettings/SettingRecords.plist normally represent?

Is the following structure expected on a normal device?

com.apple.ScreenTime:
  isInternal: true
  store: SafariStore
  active: true

com.apple.Preferences:
  isInternal: true
  store: UserSafety
  active: false
  syncToWatch: true

Can this structure exist without a user-visible Screen Time restriction?

Can this structure be related to Apple ID sign-out restriction?

What additional artifacts should be checked to confirm the source of the restriction?
Question group 3: MCState / MDM / supervision
Does IsSupervised:false rule out ordinary supervised-device management?

Does PostSetupProfileWasInstalled:false rule out a simple installed-profile explanation?

What is the significance of empty visible profile structures?

PayloadManifest:
  OrderedProfiles: []
  HiddenProfiles: []

ProfileTruth:
  {}

PayloadDependency:
  {}

Are there policy states that can restrict sign-out without visible MDM enrollment or installed profiles?

What additional MCState or configuration files should be reviewed?
Question group 4: Analytics / MDMStatus
What does MDMStatus:false in Analytics normally mean?

Does MDMStatus:false reliably indicate that the device was not MDM-enrolled?

Can an Apple ID sign-out restriction occur with MDMStatus:false?

Are there known false-negative cases for this field?

How should this field be interpreted alongside MCState and ManagedSettings artifacts?
Question group 5: Account / cloud / telecom context
Is the next-day CommCenter / Baseband / TelephonyBaseband context relevant to the restriction event?

Can carrier / baseband / CommCenter events interact with Apple ID trust or account state?

Are SFA / CKKS / CloudServices artifacts needed to determine whether account-cloud state was involved?

What minimal raw samples should be reviewed to confirm or reject account-cloud involvement?
Question group 6: Same-day side effects
Are the same-day crash / CPU / disk-write artifacts meaningful or incidental?

Do the following artifacts form a meaningful cluster?

Grab-2026-03-03-162129.ips
ospredictiond.cpu_resource-2026-03-03-163418.ips
signpost_reporter.cpu_resource-2026-03-03-164816.ips
fileproviderd.diskwrites_resource

Can these artifacts occur during normal device activity?

Are they consistent with local instability around policy / account / cloud state changes?

What additional timestamps or logs should be compared?
Question group 7: Find My auxiliary context
Are Find My / findmylocated references on this date normal?

Are they relevant to Apple ID trust or device-state evaluation?

Can they be treated only as auxiliary context?

What artifacts would be needed to make Find My a stronger line of evidence?
Question group 8: Evidence integrity
Are the SHA256 values sufficient to identify the preserved artifacts?

How should partially readable sysdiagnose archives be handled?

Should partial archives be excluded from conclusions or retained as supporting evidence?

What chain-of-custody process should be used if raw files are submitted?

Should physical device review be considered after preliminary artifact review?
Question group 9: Overall forensic significance
Is the 2026-03-03 artifact correlation technically meaningful?

Can the whole structure be explained by normal iOS behavior?

Is this likely to be a benign local policy edge case?

Does the structure justify deeper mobile forensic review?

What is the minimal next-step dataset required for a formal review?
Boundary

These questions do not assume malicious activity.

They are intended to help determine whether the observed structure is benign, explainable, abnormal, or worthy of formal forensic review.
