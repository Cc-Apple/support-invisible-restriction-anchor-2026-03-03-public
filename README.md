# Support Invisible Restriction Anchor - Public Technical Package

## Status

Public preliminary technical review package.

This repository is intended for qualified digital forensics, incident response, mobile forensic, legal-technical, or security research review.

It is not a public accusation, attribution claim, malware conclusion, or attribution claim against any vendor, country, group, or individual.

---

## Correction notice

Earlier versions of this repository incorrectly treated 2026-03-03 as the Apple Support contact date.

Correction:

- 2026-03-03 is the preserved iOS artifact / sysdiagnose anchor date.
- 2026-03-04 is an additional anchor date involving Lost Mode, Find My, Game Center UI exposure, Visual Intelligence / ANE pressure, and Account / Cloud / Trust burst observations.
- 2026-03-05 is the Apple Support interaction date.
- The Apple Support interaction window was approximately 11:10-11:31 VN time on 2026-03-05.
- The 2026-03-05 artifacts show ManagedSettings / Safari restriction changes around 11:11:38 VN time and DMD / Digital Health / Game Center-related restriction recomputation shortly afterward.
- Later on 2026-03-05, screenshots/video reportedly captured Screen Time restriction UI and Apple ID sign-out restriction behavior.

This correction does not remove the artifact value of 2026-03-03. It separates the case into three review dates:

1. 2026-03-03: FileProvider / MCState / ManagedSettings / visible-management-absent artifact anchor.
2. 2026-03-04: Lost Mode / Find My / Game Center exposure / ANE-VisualIntelligence pressure / Account-Cloud-Trust burst anchor.
3. 2026-03-05: Apple Support interaction + ManagedSettings/DMD/Game Center recomputation + later Screen Time UI evidence anchor.

---

## Public repository boundary

Raw iOS logs, raw sysdiagnose archives, raw screenshots, and raw videos are not included in this public repository.

This repository contains only:

- written technical summaries
- artifact names
- referenced log titles
- referenced sysdiagnose archive names
- SHA256 references where available
- timeline summaries
- analysis scripts
- machine-readable observation summaries
- reviewer questions

Original raw artifacts are preserved separately and may be provided later through a secure evidence-handling procedure if required by a qualified reviewer.

---

## Device label

Internal label: `15G`

Physical device class: iPhone 12 mini class device

Observed model identifier: `iPhone13,1`

Observed OS generation: iPhone OS 18.5 / 22F76

Important note:

`15G` is an internal Ghost / Apple ID lineage label. It does not mean that the physical device is an iPhone 15 Pro.

---

## Core technical question

The core question is not whether classic visible MDM was installed.

The key question is whether the observed behavior can be explained by ordinary local Screen Time / Family Sharing / ManagedSettings behavior, or whether the artifacts show an account/cloud/policy-adjacent restriction state that was not visible as ordinary MDM, supervision, or configuration profile management.

Reviewed artifacts repeatedly showed:

- `MDMStatus:false`
- `IsSupervised:false`
- `PostSetupProfileWasInstalled:false`
- empty visible profile / payload structures
- ManagedSettings / ScreenTime local stores
- DMD / Digital Health restriction recomputation
- FileProvider / SaveToFiles activity
- iCloud Drive shown as logged out / not configured in `brctl`
- FileProvider iCloud Drive provider state still present as enabled / needs-auth
- AppleAccount / CKKS / PCS / SOS / CloudServices / Networking bursts
- storage and memory-pressure context
- later visible Screen Time / sign-out restriction UI evidence on 2026-03-05

---

## Anchor summary

### 2026-03-03 - artifact anchor

The 2026-03-03 artifacts are treated as the first artifact anchor.

Key observations:

- MCState present
- `IsSupervised:false`
- `PostSetupProfileWasInstalled:false`
- visible profile / payload structures empty
- ManagedSettings / ScreenTime local stores present
- FileProvider / SaveToFiles activity present
- iCloud Drive shown as logged out / not configured in `brctl`
- FileProvider retained iCloud Drive provider state requiring authentication
- large `fileproviderd` disk-write activity
- storage and memory-pressure context
- no classic visible MDM indicator found in reviewed artifacts

This date is not the Apple Support contact date.

---

### 2026-03-04 - Lost Mode / Game Center / pressure anchor

The 2026-03-04 artifacts are treated as an independent anchor, not merely a bridge day.

Key observations:

- Apple Pay stopped notification around 04:20 VN time
- Lost Mode enabled notification around 04:21 VN time
- screenshot/video evidence reportedly preserved around 04:20-04:50 VN time
- 04:43 Game Center UI screenshot reportedly captured
- Game Center social / friends-related restriction baseline still present in MCState around 05:13
- ANECompilerService large disk-write activity
- Visual Intelligence / Photos / Spotlight / media analysis concentration
- multiple 1GB-class disk-write events across ANECompilerService, WeChat, fileproviderd, and sysdiagnosed
- Wi-Fi disassociation / WWAN state context
- late-night physical-sensation report timestamp around 23:13 VN time
- around the same time, SFA / CloudServices / CKKS / PCS / SOS / Networking burst observed

Subjective physical observations are not treated as standalone proof of an external physical source. They are used only as contemporaneous timestamp context for why the user was interacting with and observing the device.

---

### 2026-03-05 - Apple Support / ManagedSettings anchor

The 2026-03-05 artifacts are treated as the Apple Support interaction anchor.

Key observations:

- Apple Support interaction window approximately 11:10-11:31 VN time
- ManagedSettings / Safari restriction changes around 11:11:38 VN time
- DMD / Digital Health restriction recomputation shortly afterward
- Game Center social / friends-related restriction recomputation around 11:14 VN time
- Apple Support-side confirmation reportedly indicated no ordinary visible Screen Time / Family Sharing / MDM / supervision configuration matching the observed restriction state
- 18:11 VN time screenshot reportedly captured Screen Time restriction-related UI
- 18:12 VN time video reportedly captured Screen Time settings and Apple ID sign-out restriction behavior
- WeChat large disk-write pressure later the same day
- no classic visible MDM / supervision / profile indicator found in reviewed artifacts

---

## Cross-day interpretation

The three dates should be read together.

### 2026-03-03

Artifact-level visible-management absence plus FileProvider / ManagedSettings / storage-pressure context.

### 2026-03-04

Lost Mode / Find My / Game Center exposure plus ANE / Visual Intelligence / storage-pressure and Account / Cloud / Trust burst context.

### 2026-03-05

Apple Support window plus ManagedSettings / DMD / Game Center restriction recomputation and later visible Screen Time / sign-out restriction UI evidence.

Together, the observations support a technical review question:

Can an account/cloud/policy-adjacent restriction state exist or persist without ordinary visible MDM, supervision, or configuration profile indicators, and later surface through Screen Time / ManagedSettings / Apple ID sign-out restriction behavior?

This repository does not claim the answer. It preserves the question and the artifacts needed for review.

---

## TTP comparison hypothesis

This repository does not attribute the observed behavior to APT32, APT42, APT28, APT41, APT10, APT27, Pegasus, NSO Group, Apple, or any state actor.

However, for reviewer framing, the observed seam failures are compared at the TTP level with public models:

- physical-proximity Wi-Fi access models such as Evil Twin / Rogue AP techniques
- credential / trust-state capture or manipulation hypotheses
- cloud/account-focused social engineering models
- user-interaction-gated account/control workflows
- support/account workflow manipulation
- visible MDM/profile absent, but internal restriction layers present

These are comparison models only.

The current working hypothesis is:

Physical-proximity-seeded account / trust-state manipulation  
plus  
user-interaction-gated cloud/account-control workflow  
plus  
visible-management-absent internal restriction layer exposure.

This is not an attribution claim.

---

## What this repository is not

This repository is not:

- a malware sample repository
- an exploit repository
- a zero-day claim
- an attribution report
- a public accusation
- a claim that Apple intentionally performed the observed actions
- a claim that any named APT group performed the observed actions
- a claim that Evil Twin or malicious profile injection has been proven

---

## What reviewers are asked to evaluate

Reviewers are asked to evaluate:

1. Whether the absence of visible MDM / supervision / profile indicators is technically meaningful.
2. Whether ManagedSettings / DMD / Digital Health restriction recomputation around the Apple Support window is ordinary or anomalous.
3. Whether Game Center social restriction recomputation is expected in this context.
4. Whether FileProvider / iCloud Drive needs-auth state while `brctl` reports iCloud Drive not configured is ordinary or anomalous.
5. Whether 1GB-class disk-write patterns across 2026-03-03, 2026-03-04, and 2026-03-05 are ordinary low-storage behavior or a meaningful repeated pattern.
6. Whether AppleAccount / CKKS / PCS / SOS / CloudServices / Networking bursts align with normal account health reporting or suggest an unusual account/trust-state transition.
7. Whether the later Screen Time / Apple ID sign-out restriction UI evidence can be explained without ordinary visible MDM / Family Sharing / Screen Time configuration.

---

## Repository map

- `00_public_boundary/`  
  Correction notice, device label, public scope, reviewer boundary.

- `01_anchor_2026-03-03/`  
  2026-03-03 artifact anchor.

- `02_anchor_2026-03-04/`  
  2026-03-04 Lost Mode / Game Center / pressure / trust-burst anchor.

- `03_anchor_2026-03-05/`  
  2026-03-05 Apple Support / ManagedSettings / DMD / UI evidence anchor.

- `04_cross_day_correlation/`  
  Cross-day comparison and TTP hypothesis.

- `05_evidence_index/`  
  Artifact inventory, private screenshot/video index, SHA256 references.

- `06_machine_readable/`  
  YAML summaries for machine review.

- `scripts/`  
  Reproducibility scripts for event extraction and reference hashing.

---

## Review posture

The requested review is narrow:

Preserve the artifacts, test the timeline, compare normal vs abnormal interpretations, and determine whether the observed restriction state can be explained by ordinary iOS behavior.

No attribution conclusion should be drawn from this public package alone.
