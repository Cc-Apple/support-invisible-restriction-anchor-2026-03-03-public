# Correction Notice

## Summary

This repository was originally framed around 2026-03-03 as the primary Apple Support contact date.

That framing was incorrect.

The corrected structure is:

* 2026-03-03: artifact / FileProvider / MCState / ManagedSettings anchor
* 2026-03-04: Lost Mode / Find My / Game Center / ANE-VisualIntelligence / Account-Cloud-Trust burst anchor
* 2026-03-05: Apple Support interaction / ManagedSettings-DMD-Game Center recomputation / later Screen Time UI evidence anchor

---

## Corrected Apple Support date

The Apple Support interaction did not occur on 2026-03-03.

The Apple Support interaction occurred on 2026-03-05.

Approximate support interaction window:

`2026-03-05 11:10-11:31 VN time`

This time window is important because the reviewed device artifacts show ManagedSettings / DMD / Digital Health / Game Center-related restriction changes in the same general time window.

---

## Corrected role of 2026-03-03

2026-03-03 remains important.

It should be treated as the first artifact anchor.

Key relevance:

* MCState present
* ManagedSettings present
* visible MDM indicators absent
* visible profile / supervision indicators absent
* FileProvider / SaveToFiles activity present
* iCloud Drive shown as logged out / not configured in `brctl`
* FileProvider iCloud Drive provider state still present as enabled / needs-auth
* fileproviderd large disk-write pressure
* memory / storage pressure context

However, 2026-03-03 should not be described as the Apple Support contact date.

---

## Corrected role of 2026-03-04

2026-03-04 is now treated as an independent anchor, not a minor bridge day.

Key relevance:

* Apple Pay stopped notification around 04:20 VN time
* Lost Mode enabled notification around 04:21 VN time
* Find My / Family / AppleAccount-related context
* Game Center UI exposure around 04:43 VN time
* Game Center social restriction baseline still present around 05:13 VN time
* ANECompilerService / Visual Intelligence / Photos / Spotlight pressure
* multiple 1GB-class disk-write events
* late-night physical-sensation report around 23:13 VN time
* same-time SFA / CloudServices / CKKS / PCS / SOS / Networking burst

Subjective observations are included only as timestamp context.

They are not treated as standalone proof of an external physical source.

---

## Corrected role of 2026-03-05

2026-03-05 is the Apple Support interaction anchor.

Key relevance:

* Apple Support interaction window around 11:10-11:31 VN time
* ManagedSettings / Safari restriction changes around 11:11:38 VN time
* DMD / Digital Health restriction recomputation shortly afterward
* Game Center social / friends-related restriction recomputation around 11:14 VN time
* later screenshot/video evidence reportedly captured Screen Time restriction UI and Apple ID sign-out restriction behavior around 18:11-18:12 VN time
* WeChat large disk-write pressure later the same day
* reviewed artifacts did not show classic visible MDM / supervision / profile indicators

---

## Why this correction matters

The correction changes the structure of the case.

The issue is not a single-day 2026-03-03 event.

The corrected structure is a three-day sequence:

1. 2026-03-03 shows visible-management-absent artifact and FileProvider / storage-pressure behavior.
2. 2026-03-04 shows Lost Mode / Game Center / Visual Intelligence / pressure / Account-Cloud-Trust burst behavior.
3. 2026-03-05 shows Apple Support interaction aligned with ManagedSettings / DMD / Game Center recomputation and later visible Screen Time restriction evidence.

This correction improves the technical clarity of the package.

It does not remove the artifact value of 2026-03-03.

---

## Non-attribution boundary

This correction does not add any attribution claim.

It does not claim:

* a specific actor
* a specific malware family
* a specific exploit
* a specific Evil Twin or Rogue AP proof
* a specific malicious profile proof
* a specific Apple-side cause

It only corrects the timeline and separates artifact roles by date.

---

## Reviewer guidance

Reviewers should evaluate the corrected sequence as:

* artifact continuity
* ManagedSettings / MCState behavior
* DMD / Digital Health recomputation
* Game Center social restriction behavior
* FileProvider / iCloud Drive needs-auth behavior
* Account / CKKS / CloudServices / PCS / SOS bursts
* Screen Time / Apple ID sign-out UI evidence

The public package should not be treated as final proof without private raw artifact review.
