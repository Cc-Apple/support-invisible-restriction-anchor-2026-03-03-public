# Reviewer Scope

## Purpose

This file defines what qualified reviewers are asked to evaluate.

This repository is a public technical review package.

It is not an attribution report.

It is not a malware conclusion.

It is not a claim that a specific actor, vendor, country, group, or individual caused the observed behavior.

---

## Review target

The review target is the three-anchor sequence:

1. `2026-03-03`

   * FileProvider / MCState / ManagedSettings / visible-management-absent artifact anchor

2. `2026-03-04`

   * Lost Mode / Find My / Game Center exposure / ANE-VisualIntelligence pressure / Account-Cloud-Trust burst anchor

3. `2026-03-05`

   * Apple Support interaction / ManagedSettings-DMD-Game Center recomputation / later Screen Time UI evidence anchor

---

## Primary review questions

Reviewers are asked to evaluate the following questions.

### 1. Visible management state

Do the reviewed artifacts support the absence of ordinary visible management indicators?

Relevant indicators include:

* `MDMStatus:false`
* `IsSupervised:false`
* `PostSetupProfileWasInstalled:false`
* empty `MCProfileEvents`
* empty visible `PayloadManifest` / profile structures

Question:

Can the later Screen Time / Apple ID sign-out restriction behavior be explained if ordinary visible MDM, supervision, or configuration profile indicators are absent?

---

### 2. ManagedSettings / DMD behavior

Do the reviewed artifacts show meaningful ManagedSettings / DMD / Digital Health restriction behavior?

Relevant observations include:

* ManagedSettings / ScreenTime local stores
* Safari restriction changes around `2026-03-05 11:11:38 VN`
* DMD / Digital Health recomputation shortly afterward
* Game Center social / friends-related restriction recomputation around `2026-03-05 11:14 VN`

Question:

Is this sequence ordinary iOS behavior, or does it suggest an unusual internal restriction-state transition?

---

### 3. Apple Support window alignment

Does the Apple Support interaction window align meaningfully with the ManagedSettings / DMD events?

Known public summary:

* Apple Support interaction window: approximately `2026-03-05 11:10-11:31 VN`
* ManagedSettings / Safari restriction change: around `2026-03-05 11:11:38 VN`
* DMD / Digital Health / Game Center recomputation: around `2026-03-05 11:14 VN`

Question:

Is the timing alignment explainable as ordinary background state change, or does it require deeper review?

---

### 4. Game Center restriction behavior

Does the Game Center social restriction behavior have normal explanation in this context?

Relevant observations include:

* Game Center UI exposure reportedly captured around `2026-03-04 04:43 VN`
* Game Center social / friends restriction baseline still present around `2026-03-04 05:13 VN`
* Game Center-related restriction recomputation around `2026-03-05 11:14 VN`

Question:

Why would Game Center social / friends-related restriction keys appear and recompute in this timeline, especially for a user who does not use Game Center as a primary activity?

---

### 5. FileProvider / iCloud Drive state

Does the FileProvider / iCloud Drive state represent ordinary behavior?

Relevant observations include:

* `brctl` reports iCloud Drive logged out / not configured
* FileProvider still retains an iCloud Drive provider state
* iCloud Drive FileProvider state appears enabled / needs-auth
* LocalStorageFileProvider / SaveToFiles activity appears in relevant windows

Question:

Is this expected behavior for iCloud Drive not configured, or does it suggest a trust-state or account-state edge case?

---

### 6. Storage-pressure pattern

Are the repeated 1GB-class disk-write events ordinary low-storage behavior or a meaningful repeated pattern?

Relevant observations include:

* 2026-03-03: large `fileproviderd` disk-write event
* 2026-03-04: multiple 1GB-class disk-write events involving ANECompilerService, WeChat, fileproviderd, and sysdiagnosed
* 2026-03-05: large WeChat disk-write event

Question:

Are these events expected under low-storage / normal background processing, or do they indicate a repeated pressure pattern worth deeper review?

---

### 7. Account / Cloud / Trust bursts

Do AppleAccount / CKKS / PCS / SOS / CloudServices / Networking bursts represent ordinary account health reporting?

Relevant observations include:

* SFA / CloudServices / CKKS / PCS / SOS / Networking records around key windows
* account / trust / keychain-related records
* private screenshot/video context preserved separately

Question:

Are these records consistent with normal Apple account health reporting, or do they suggest an unusual account/trust-state transition?

---

### 8. Screenshot and video evidence alignment

Do the private screenshot/video timestamps align with the log-derived timeline?

Relevant private evidence categories include:

* Lost Mode / Apple Pay stopped notifications around `2026-03-04 04:20-04:21 VN`
* Game Center UI screenshot around `2026-03-04 04:43 VN`
* physical-sensation report screenshot around `2026-03-04 23:13 VN`
* Apple Support-related context on `2026-03-05`
* Screen Time restriction screenshot around `2026-03-05 18:11 VN`
* Screen Time settings / Apple ID sign-out restriction video around `2026-03-05 18:12 VN`

Question:

Do these UI evidence timestamps support the three-anchor interpretation?

---

## Out of scope

The following are out of scope for this public package:

* final actor attribution
* country attribution
* vendor accusation
* malware-family conclusion
* zero-day conclusion
* Pegasus conclusion
* proof of Evil Twin / Rogue AP use
* proof of malicious profile injection
* proof of classic MDM enrollment

These may be reviewer hypotheses, but they are not public-package conclusions.

---

## Requested reviewer output

A useful reviewer response would separate findings into:

1. Confirmed normal behavior
2. Confirmed anomalous behavior
3. Insufficient evidence
4. Requires raw artifact review
5. Requires Apple-side records
6. Requires screenshot/video timestamp verification
7. Requires device-side reproduction or comparison device testing

---

## Private artifact request guidance

If a reviewer requires private artifacts, they should specify:

* exact artifact name
* date
* reason public summary is insufficient
* whether redacted extract is enough
* whether SHA256 verification is required
* how the artifact will be protected

Raw artifacts should not be requested broadly without a clear review purpose.

---

## Final note

The goal is not to prove a predetermined conclusion.

The goal is to test whether the observed sequence can be explained by ordinary iOS behavior, or whether it requires deeper Apple account / ManagedSettings / DMD / FileProvider / trust-state review.
