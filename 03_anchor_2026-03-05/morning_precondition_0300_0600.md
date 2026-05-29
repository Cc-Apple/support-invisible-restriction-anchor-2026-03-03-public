# Morning Precondition Window - 2026-03-05 03:00-06:00 UTC+7

## Purpose

This file summarizes the early-morning precondition window on 2026-03-05.

All times in this file are local device-observation time, UTC+7.

Window:

`2026-03-05 03:00-06:00 UTC+7`

This window is not treated as the direct restriction-change window.

The direct restriction-change window appears later around:

`2026-03-05 11:11-11:14 UTC+7`

---

## Summary

The 03:00-06:00 window showed device-state activity before the later Apple Support and ManagedSettings / DMD recomputation window.

Public summary:

* background processing concentration
* SiriSearchFeedback / Visual Intelligence / Photos context
* ScreenTimeAgent cleanup context
* Wi-Fi / Cellular / Wi-Fi-like route changes
* battery / thermal context
* user-interaction context
* system indexing / maintenance context

Interpretation:

This window is treated as a precondition / device-state preparation window.

It is not treated as direct proof of the later 11:11 ManagedSettings change.

---

## Key observation

The main technical value of this window is that the device was not static.

The reviewed artifacts suggest that the device state, background processing state, and network route state changed before the later Apple Support interaction window.

This may be ordinary early-morning iOS maintenance.

It may also be relevant because the later 11:11-11:14 restriction-state transition occurred the same day.

---

## Background-processing concentration

Reviewed artifacts showed background activity involving categories such as:

* RAPID.DataCollectionActivity
* rtcreportingd cleanup context
* cloudphotod sync context
* assetsd background activity
* spotlightknowledged context
* mediaanalysis / photoanalysis context
* anomalydetectiond context
* Proactive / Siri / Search-related context
* ScreenTimeAgent cleanup context

Interpretation:

These are not individually abnormal.

The concentration is relevant because it appears before the Apple Support / ManagedSettings recomputation window.

---

## SiriSearchFeedback / Visual Intelligence / Photos context

The 03:00-06:00 window showed SiriSearchFeedback and related activity.

Relevant public categories:

* Visual Intelligence
* Photos
* Spotlight
* parsecd
* Siri / Search feedback context

Interpretation:

This may reflect ordinary indexing, Photos analysis, search feedback, or visual feature maintenance.

It is still relevant as part of the same-day precondition timeline.

---

## ScreenTimeAgent cleanup context

ScreenTimeAgent cleanup activity appeared in the early-morning window.

Public interpretation:

This does not prove that Screen Time restrictions were applied in this window.

It is important because later the same day, ManagedSettings / DMD / Digital Health restriction recomputation appeared around the Apple Support window.

Sequence:

1. Early morning: ScreenTimeAgent cleanup context.
2. 11:11-11:14 UTC+7: ManagedSettings / DMD restriction-state transition.
3. 18:11-18:12 UTC+7: later Screen Time / Apple ID sign-out restriction UI evidence reportedly captured.

---

## Network route changes

Reviewed artifacts indicated network-route changes during the early-morning window.

Public summary:

* Wi-Fi route observed at one point
* Cellular / WWAN route observed at another point
* route later appeared to return to Wi-Fi-like path in available network records

Interpretation:

This may be ordinary network switching.

It is relevant because physical-proximity / Wi-Fi / account-control hypotheses depend on route and interaction timing.

Precise BSSID / SSID / location-sensitive values are not published in this repository.

---

## Battery and thermal context

The early-morning window included battery / thermal context.

Public summary:

* battery drain context appeared in the reviewed records
* thermal pressure context appeared during the window
* device was active enough to generate relevant logs and sysdiagnose-related data

Interpretation:

This supports that the device was under workload or active-state change during the precondition window.

---

## User-interaction interpretation

This window may support a user-interaction-gated model.

Possible interpretation:

* the user interacted with or checked the device
* the device became active / foregrounded
* network route and background processing changed
* system/account/restriction-related processes had preconditions before later 11:11-11:14 restriction recomputation

This is only a hypothesis.

It does not prove external causation.

---

## Relation to Apple Support window

The early-morning window precedes:

`2026-03-05 11:10-11:31 UTC+7`

Apple Support interaction window.

The relationship is:

* 03:00-06:00: precondition / device-state window
* 11:10-11:31: Apple Support interaction window
* 11:11-11:14: ManagedSettings / DMD / Game Center recomputation window
* 18:11-18:12: later Screen Time / sign-out restriction UI evidence window

---

## Normal interpretation

Possible normal explanations include:

* normal early-morning iOS maintenance
* Photos / Spotlight / Visual Intelligence indexing
* ScreenTimeAgent cleanup
* network route switching
* battery / thermal effects from ordinary background processing
* ordinary Siri / Search feedback generation

---

## Anomalous interpretation

This window remains relevant because:

* it appears on the same date as the Apple Support / ManagedSettings anchor
* it includes ScreenTimeAgent cleanup context before later restriction recomputation
* it includes network route changes before the support window
* it includes background processing concentration
* it may represent a device-state preparation window rather than the main restriction-change event

---

## Boundary

This file does not prove:

* malware
* actor attribution
* Evil Twin / Rogue AP use
* malicious profile injection
* classic MDM enrollment
* Apple-side causation
* external physical source
* direct restriction application during 03:00-06:00

This file only documents the early-morning precondition window for technical review.
