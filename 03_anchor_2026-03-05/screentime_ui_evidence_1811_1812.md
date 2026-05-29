# Screen Time UI Evidence - 2026-03-05 18:11-18:12 UTC+7

## Purpose

This file summarizes the later Screen Time / Apple ID sign-out restriction UI evidence from 2026-03-05.

All times in this file are local device-observation time, UTC+7.

Key window:

`2026-03-05 18:11-18:12 UTC+7`

Raw screenshots and videos are not included in this public repository.

They are preserved privately.

---

## Summary

Later on 2026-03-05, user-side screenshot/video evidence reportedly captured visible restriction behavior.

Public summary:

* `2026-03-05 18:11 UTC+7`

  * Screen Time restriction-related UI screenshot reportedly captured.

* `2026-03-05 18:12 UTC+7`

  * video reportedly captured Screen Time settings and Apple ID sign-out restriction behavior.

This window is important because it appears after the earlier 11:11-11:14 UTC+7 ManagedSettings / DMD / Game Center recomputation window.

---

## 18:11 UTC+7 screenshot context

Reported private evidence:

* Screen Time restriction-related UI screenshot
* Screen Time passcode / restriction-related field visible

Public interpretation:

This screenshot is treated as user-side UI evidence that a restriction-related Screen Time state was visible later on the same date.

The raw screenshot is not public because it may contain private account or device information.

---

## 18:12 UTC+7 video context

Reported private evidence:

* video showing Screen Time settings
* video showing relevant Screen Time configuration items
* video showing Apple ID sign-out restriction behavior

Public interpretation:

This video is one of the strongest user-side UI anchors for 2026-03-05.

It is relevant because reviewed device artifacts earlier the same day showed ManagedSettings / DMD / Digital Health / Game Center recomputation around the Apple Support interaction window.

---

## Relation to 11:11-11:14 UTC+7 artifact window

Earlier on the same day, reviewed artifacts showed:

* ManagedSettings / Safari restriction changes around `11:11:38 UTC+7`
* DMD / Digital Health recomputation shortly afterward
* Game Center social / friends-related restriction recomputation around `11:14 UTC+7`

The 18:11-18:12 UI evidence appears later on the same day.

Interpretation:

This creates a candidate sequence:

1. `11:10-11:31 UTC+7`

   * Apple Support interaction window.

2. `11:11-11:14 UTC+7`

   * ManagedSettings / DMD / Game Center recomputation window.

3. `18:11-18:12 UTC+7`

   * visible Screen Time / Apple ID sign-out restriction UI evidence.

This sequence is one of the main reasons 2026-03-05 is treated as an anchor date.

---

## Relation to visible management absence

Reviewed artifacts did not show ordinary visible MDM / supervision / configuration profile indicators.

Public summary:

* `MDMStatus:false`
* `IsSupervised:false`
* `PostSetupProfileWasInstalled:false`
* `MCProfileEvents: []`
* visible profile / payload structures empty

Review question:

Can the 18:11-18:12 Screen Time / sign-out restriction UI evidence be explained by ordinary visible Screen Time / Family Sharing / MDM / supervision state?

This repository does not answer that question.

It preserves the timeline for qualified review.

---

## Relation to Apple Support confirmation

User-side records reportedly indicate that Apple Support-side confirmation did not show ordinary visible Screen Time / Family Sharing / MDM / supervision state matching the observed restriction behavior.

Public boundary:

Raw Apple Support screenshots, support-case details, and account identifiers are not public.

They are preserved privately.

Interpretation:

The Apple Support-side context should be reviewed together with the 18:11-18:12 UI evidence and the 11:11-11:14 artifact window.

---

## Normal interpretation

Possible normal explanations include:

* ordinary Screen Time / Family Sharing behavior
* ordinary local Screen Time passcode or restriction state
* ordinary Apple ID sign-out restriction due to Screen Time settings
* normal delay between internal settings change and UI observation
* user/account configuration not visible in the public artifact summary

---

## Anomalous interpretation

This evidence remains important because:

* the UI evidence appears after the 11:11-11:14 ManagedSettings / DMD recomputation window
* the same day includes an Apple Support interaction window
* reviewed artifacts did not show classic visible MDM / supervision / profile indicators
* Apple Support-side confirmation reportedly did not match ordinary visible Screen Time / Family Sharing / MDM / supervision state
* 2026-03-03 and 2026-03-04 provide earlier baseline and pressure / Game Center context

---

## Private verification required

A qualified reviewer may request private evidence to verify:

* screenshot timestamp
* video timestamp
* visible UI state
* Apple ID sign-out restriction message
* Screen Time settings visible in the recording
* whether personal information can be redacted before review
* whether hash-based verification is available

Raw screenshot and video evidence should not be posted publicly.

---

## Boundary

This file does not prove:

* malware
* actor attribution
* Evil Twin / Rogue AP use
* malicious profile injection
* classic MDM enrollment
* Apple-side causation
* that Apple Support caused the restriction behavior

This file documents the later Screen Time / Apple ID sign-out restriction UI evidence window for technical review.
