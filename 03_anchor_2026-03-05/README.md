# 2026-03-05 Apple Support / ManagedSettings Anchor

## Purpose

This directory summarizes the 2026-03-05 anchor.

This date is the Apple Support interaction date.

The key window is:

`2026-03-05 11:10-11:31 VN time`

This date is treated as the strongest ManagedSettings / DMD / Game Center recomputation anchor.

---

## Anchor classification

`2026-03-05` is classified as:

`Apple Support interaction / ManagedSettings-DMD-Game Center recomputation / later Screen Time UI evidence anchor`

---

## Why this date matters

2026-03-05 matters because three evidence lines align:

1. Apple Support interaction window
2. Device-side ManagedSettings / DMD / Digital Health / Game Center recomputation
3. Later Screen Time / Apple ID sign-out restriction UI evidence

Public summary:

* Apple Support interaction occurred around 11:10-11:31 VN time
* ManagedSettings / Safari restriction changes appeared around 11:11:38 VN time
* DMD / Digital Health / Game Center restriction recomputation appeared shortly afterward
* Screen Time restriction UI screenshot reportedly captured around 18:11 VN time
* Screen Time settings / Apple ID sign-out restriction video reportedly captured around 18:12 VN time

---

## Apple Support window

The Apple Support interaction window was approximately:

`2026-03-05 11:10-11:31 VN time`

Public interpretation:

This is the main external timing anchor for the date.

The important point is not only that Apple Support was contacted.

The important point is that device-side ManagedSettings / DMD / Digital Health / Game Center restriction events appear inside or immediately near the same support window.

---

## ManagedSettings / Safari restriction change

Around `2026-03-05 11:11:38 VN time`, reviewed artifacts showed ManagedSettings / Safari restriction changes.

Relevant restriction areas:

* Safari private browsing
* Safari history clearing

Public summary:

* Safari private browsing restriction changed
* Safari history clearing restriction changed
* EffectiveUserSettings recomputation followed

Interpretation:

This is one of the core 2026-03-05 artifact events.

---

## DMD / Digital Health recomputation

Shortly after the ManagedSettings event, DMD / Digital Health restriction recomputation appeared.

Relevant public categories:

* DMD
* Digital Health restrictions
* EffectiveUserSettings recomputation
* app restriction lists
* Game Center social / friends-related restrictions
* media / ratings-related restrictions

Interpretation:

The DMD / Digital Health recomputation is the second core artifact event for the Apple Support window.

---

## Game Center recomputation

Game Center social / friends-related restrictions were recomputed around the Apple Support window.

Relevant restriction areas:

* adding Game Center friends
* Game Center friends sharing modification
* Game Center private messaging
* Game Center profile modification
* Game Center player-type restrictions

Why this matters:

* Game Center UI exposure was reportedly captured on 2026-03-04.
* Game Center social restriction baseline was still present on 2026-03-04.
* Game Center-related restrictions were recomputed on 2026-03-05 around the Apple Support window.

Interpretation:

Game Center is treated as a possible exposed seam in the internal restriction template.

It is not treated as the main target.

---

## Later UI evidence

Later on 2026-03-05, user-side screenshot/video evidence reportedly captured visible restriction behavior.

Public summary:

### Around 18:11 VN

Screen Time restriction-related UI screenshot reportedly captured.

### Around 18:12 VN

Video reportedly captured:

* Screen Time settings
* relevant Screen Time-related items
* Apple ID sign-out restriction behavior

Raw screenshots and videos are preserved privately.

They are not included in this public repository.

---

## Morning precondition window

The early-morning window around `03:00-06:00 VN` is also relevant.

Public summary:

* background processing concentration
* SiriSearchFeedback / Visual Intelligence / Photos context
* ScreenTimeAgent cleanup context
* Wi-Fi / Cellular / Wi-Fi-like route changes
* battery / thermal context
* device interaction context

Interpretation:

This is treated as a precondition / preparation / device-state window.

It is not treated as the direct restriction-change window.

The direct restriction-change window is around 11:11-11:14 VN time.

---

## Storage-pressure context

2026-03-05 also included large WeChat disk-write pressure.

Public summary:

* WeChat 1GB-class disk-write event
* low free storage context
* crash / log writing context
* communication / financial / mail / screenshot-related app context in nearby records

Interpretation:

This should be compared with:

* 2026-03-03 fileproviderd 1GB-class disk-write event
* 2026-03-04 multiple 1GB-class disk-write events

---

## Visible management state

Reviewed artifacts continued to support the absence of classic visible management indicators.

Public summary:

* `MDMStatus:false`
* `IsSupervised:false`
* `PostSetupProfileWasInstalled:false`
* `MCProfileEvents: []`
* visible profile / payload structures empty

Interpretation:

The key question is how Screen Time / ManagedSettings / Apple ID sign-out restriction behavior surfaced without ordinary visible MDM / supervision / profile indicators.

---

## Normal interpretation

Possible normal explanations include:

* ordinary Apple Support interaction with unrelated background restriction recomputation
* normal ManagedSettings / DMD / Digital Health maintenance
* normal Screen Time / Family Sharing / Game Center restriction behavior
* ordinary WeChat storage pressure
* low-storage effects causing app crashes and log-writing failures
* normal account health reporting

---

## Anomalous interpretation

This date remains important because:

* Apple Support interaction time aligns closely with ManagedSettings / DMD events
* Safari restriction changes occurred during the support window
* Game Center social restriction recomputation occurred shortly afterward
* later visible Screen Time / Apple ID sign-out restriction UI evidence exists privately
* classic visible MDM / supervision / profile indicators were not observed
* WeChat large disk-write pressure occurred later the same day
* 2026-03-03 and 2026-03-04 show related baseline / pressure / account-cloud context

---

## What this date does not prove

2026-03-05 does not prove:

* malware
* actor attribution
* Evil Twin / Rogue AP use
* malicious profile injection
* classic MDM enrollment
* Apple-side causation
* that Apple Support caused the device-side events
* that Game Center was the main target

The value of this date is the timing alignment between Apple Support interaction, ManagedSettings / DMD / Game Center recomputation, and later UI restriction evidence.

---

## Files in this directory

* `timeline_2026-03-05.md`
  Human-readable timeline for the date.

* `apple_support_window_1110_1131_vn.md`
  Apple Support interaction window and alignment summary.

* `managedsettings_dmd_gamecenter_1111_1114.md`
  ManagedSettings / DMD / Digital Health / Game Center recomputation summary.

* `morning_precondition_0300_0600.md`
  Early-morning precondition and device-state summary.

* `screentime_ui_evidence_1811_1812.md`
  Later Screen Time / Apple ID sign-out restriction UI evidence summary.

* `referenced_artifacts_2026-03-05.md`
  Public artifact reference index. Raw artifacts are not included.
