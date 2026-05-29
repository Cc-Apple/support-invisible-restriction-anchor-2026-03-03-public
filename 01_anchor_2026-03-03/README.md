# 2026-03-03 Artifact Anchor

## Purpose

This directory summarizes the 2026-03-03 artifact anchor.

This date is not the Apple Support contact date.

The role of this date is to preserve the first reviewed artifact anchor showing:

* visible management indicators absent
* MCState / ManagedSettings present
* FileProvider / SaveToFiles activity
* iCloud Drive shown as not configured in `brctl`
* FileProvider iCloud Drive provider state still present as enabled / needs-auth
* storage and memory-pressure context
* large `fileproviderd` disk-write activity

---

## Anchor classification

`2026-03-03` is classified as:

`FileProvider / MCState / ManagedSettings / visible-management-absent artifact anchor`

---

## Reviewed artifact groups

The reviewed 2026-03-03 artifacts include:

* local log ZIP
* multiple sysdiagnose archives
* stackshot records
* FileProvider records
* MCState records
* ManagedSettings records
* brctl / iCloud Drive records
* Analytics records
* RTCReporting / AppleAccount-related records
* disk-write resource records
* memory-pressure records

Raw artifacts are not included in this public repository.

---

## Visible management state

Reviewed artifacts showed no ordinary visible management indicators.

Observed summary:

* `MDMStatus:false`
* `IsSupervised:false`
* `PostSetupProfileWasInstalled:false`
* `MCProfileEvents: []`
* visible `PayloadManifest` / profile structures empty

Interpretation:

This does not prove that no account/cloud/policy-adjacent restriction state existed.

It only means that classic visible MDM / supervision / configuration profile management was not observed in the reviewed artifacts.

---

## ManagedSettings / MCState state

MCState and ManagedSettings artifacts were present.

Key points:

* ManagedSettings / ScreenTime local stores existed
* ScreenTime / SafariStore records existed
* `ScreenTimeEnabled_CurrentUser` was empty
* Safari private browsing / history clearing restrictions were not yet enabled on this date
* EffectiveUserSettings existed and contained many restriction keys
* classic visible MDM profile structures were empty

Interpretation:

The date is important because it shows internal restriction-evaluation structures while visible management indicators were absent.

---

## FileProvider / iCloud Drive state

The reviewed artifacts showed a notable FileProvider / iCloud Drive state.

Observed summary:

* `brctl` reported iCloud Drive as logged out / not configured
* FileProvider still retained an iCloud Drive provider state
* iCloud Drive FileProvider state appeared enabled / needs-auth
* LocalStorageFileProvider / SaveToFiles activity was present

Interpretation:

This may be ordinary edge-case behavior for iCloud Drive not configured.

It may also be relevant to account/trust-state review because the FileProvider state did not simply disappear when `brctl` reported iCloud Drive as not configured.

This requires qualified review.

---

## Storage and memory pressure

The 2026-03-03 artifacts included strong storage / memory-pressure context.

Key observation:

* large `fileproviderd` disk-write activity
* low free storage context
* stackshot memory-pressure progression
* FileProvider / CloudDocs / cloudd / deleted / searchd / triald / parsecd / appleaccountd / accountsd context around the same day

Interpretation:

This date is important as the first storage-pressure anchor.

It should be compared against 2026-03-04 and 2026-03-05, where additional large disk-write and pressure events appear.

---

## What this date does not prove

2026-03-03 does not prove:

* classic MDM enrollment
* supervision
* visible configuration profile installation
* Apple Support contact
* malware
* Evil Twin / Rogue AP use
* malicious profile injection
* actor attribution

The value of this date is artifact structure, not attribution.

---

## Why 2026-03-03 matters

2026-03-03 matters because it provides the baseline condition:

Visible management indicators were absent, but internal restriction-related and FileProvider/account-related structures were present.

This baseline becomes important when compared with:

* 2026-03-04 Lost Mode / Game Center / pressure / Account-Cloud-Trust burst observations
* 2026-03-05 Apple Support window and ManagedSettings / DMD / Game Center recomputation

---

## Files in this directory

* `timeline_2026-03-03.md`
  Human-readable timeline for the date.

* `mcstate_managedsettings_summary.md`
  MCState / ManagedSettings / visible-management summary.

* `fileprovider_storage_pressure.md`
  FileProvider / storage / memory-pressure summary.

* `referenced_artifacts_2026-03-03.md`
  Public index of referenced artifacts. Raw artifacts are not included.
