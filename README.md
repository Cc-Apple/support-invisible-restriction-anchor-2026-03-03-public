# Support Invisible Restriction Anchor - Public Technical Package

## Status

Public preliminary technical review package.

This repository is intended for qualified digital forensics, incident response, mobile forensic, legal-technical, or security research review.

It is not a public accusation, attribution claim, malware conclusion, or attribution claim against any vendor, country, group, or individual.

---

## Correction notice

Earlier versions of this repository incorrectly treated 2026-03-03 as the Apple Support contact date.

Correction:

* 2026-03-03 is the preserved iOS artifact / sysdiagnose anchor date.
* 2026-03-04 is an additional anchor date involving Lost Mode, Find My, Game Center UI exposure, Visual Intelligence / ANE pressure, and Account / Cloud / Trust burst observations.
* 2026-03-05 is the Apple Support interaction date.
* The Apple Support interaction window was approximately 11:10-11:31 UTC+7 on 2026-03-05.
* The 2026-03-05 artifacts show ManagedSettings / Safari restriction changes around 11:11:38 UTC+7 and DMD / Digital Health / Game Center-related restriction recomputation shortly afterward.
* Later on 2026-03-05, screenshots/video reportedly captured Screen Time restriction UI and Apple ID sign-out restriction behavior.

This correction does not remove the artifact value of 2026-03-03. It separates the case into three review dates:

1. 2026-03-03: FileProvider / MCState / ManagedSettings / visible-management-absent artifact anchor.
2. 2026-03-04: Lost Mode / Find My / Game Center exposure / ANE-VisualIntelligence pressure / Account-Cloud-Trust burst anchor.
3. 2026-03-05: Apple Support interaction + ManagedSettings/DMD/Game Center recomputation + later Screen Time UI evidence anchor.

---

## Public repository boundary

Raw iOS logs, raw sysdiagnose archives, raw screenshots, and raw videos are not included in this public repository.

This repository contains only:

* written technical summaries
* artifact names
* referenced log titles
* referenced sysdiagnose archive names
* SHA256 references where available
* timeline summaries
* analysis scripts
* machine-readable observation summaries
* reviewer questions

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

* `MDMStatus:false`
* `IsSupervised:false`
* `PostSetupProfileWasInstalled:false`
* empty visible profile / payload structures
* ManagedSettings / ScreenTime local stores
* DMD / Digital Health restriction recomputation
* FileProvider / SaveToFiles activity
* iCloud Drive shown as logged out / not configured in `brctl`
* FileProvider iCloud Drive provider state still present as enabled / needs-auth
* AppleAccount / CKKS / PCS / SOS / CloudServices / Networking bursts
* storage and memory-pressure context
* later visible Screen Time / sign-out restriction UI evidence on 2026-03-05

---

## Anchor summary

### 2026-03-03 - artifact anchor

The 2026-03-03 artifacts are treated as the first artifact anchor.

Key observations:

* MCState present
* `IsSupervised:false`
* `PostSetupProfileWasInstalled:false`
* visible profile / payload structures empty
* ManagedSettings / ScreenTime local stores present
* FileProvider / SaveToFiles activity present
* iCloud Drive shown as logged out / not configured in `brctl`
* FileProvider retained iCloud Drive provider state requiring authentication
* large `fileproviderd` disk-write activity
* storage and memory-pressure context
* no classic visible MDM indicator found in reviewed artifacts

This date is not the Apple Support contact date.

---

### 2026-03-04 - Lost Mode / Game Center / pressure anchor

The 2026-03-04 artifacts are treated as an independent anchor, not merely a bridge day.

Key observations:

* Apple Pay stopped notification around 04:20 UTC+7
* Lost Mode enabled notification around 04:21 UTC+7
* screenshot/video evidence reportedly preserved around 04:20-04:50 UTC+7
* 04:43 UTC+7 Game Center UI screenshot reportedly captured
* Game Center social / friends-related restriction baseline still present in MCState around 05:13 UTC+7
* ANECompilerService large disk-write activity
* Visual Intelligence / Photos / Spotlight / media analysis concentration
* multiple 1GB-class disk-write events across ANECompilerService, WeChat, fileproviderd, and sysdiagnosed
* Wi-Fi disassociation / WWAN state context
* late-night physical-sensation report timestamp around 23:13 UTC+7
* around the same time, SFA / CloudServices / CKKS / PCS / SOS / Networking burst observed

Subjective physical observations are not treated as standalone proof of an external physical source. They are used only as contemporaneous timestamp context for why the user was interacting with and observing the device.

---

### 2026-03-05 - support-window anchor

The 2026-03-05 artifacts are treated as the Apple Support interaction anchor.

Key observations:

* Apple Support interaction window around 11:10-11:31 UTC+7
* ManagedSettings / Safari restriction changes around 11:11:38 UTC+7
* DMD / Digital Health restriction recomputation shortly afterward
* Game Center social / friends-related restriction recomputation around 11:14 UTC+7
* Apple Support-side confirmation reportedly indicated no ordinary visible Screen Time / Family Sharing / MDM / supervision configuration matching the observed restriction state
* 18:11 UTC+7 screenshot reportedly captured Screen Time restriction-related UI
* 18:12 UTC+7 video reportedly captured Screen Time settings and Apple ID sign-out restriction behavior
* WeChat large disk-write pressure later the same day
* no classic visible MDM / supervision / profile indicator found in reviewed artifacts

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

* physical-proximity Wi-Fi access models such as Evil Twin / Rogue AP techniques
* credential / trust-state capture or manipulation hypotheses
* cloud/account-focused social engineering models
* user-interaction-gated account/control workflows
* support/account workflow manipulation
* visible MDM/profile absent, but internal restriction layers present

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

* a malware sample repository
* an exploit repository
* a zero-day claim
* an attribution report
* a public accusation
* a claim that Apple intentionally performed the observed actions
* a claim that any named APT group performed the observed actions
* a claim that Evil Twin or malicious profile injection has been proven

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

* `00_public_boundary/`
  Correction notice, device label, public scope, reviewer boundary.

* `01_anchor_2026-03-03/`
  2026-03-03 artifact anchor.

* `02_anchor_2026-03-04/`
  2026-03-04 Lost Mode / Game Center / pressure / trust-burst anchor.

* `03_anchor_2026-03-05/`
  2026-03-05 Apple Support / ManagedSettings / DMD / UI evidence anchor.

* `04_cross_day_correlation/`
  Cross-day comparison and TTP hypothesis.

* `05_evidence_index/`
  Artifact inventory, private screenshot/video index, SHA256 references.

* `06_machine_readable/`
  YAML summaries for machine review.

* `scripts/`
  Reproducibility scripts for event extraction and reference hashing.

---

## Review posture

The requested review is narrow:

Preserve the artifacts, test the timeline, compare normal vs abnormal interpretations, and determine whether the observed restriction state can be explained by ordinary iOS behavior.

No attribution conclusion should be drawn from this public package alone.

---

## Shadow Cloud Hypothesis Mapping

This repository is a focused technical anchor for the invisible / support-adjacent restriction layer.

It should be read as a supporting package for the main Shadow Cloud working model, not as a standalone attribution claim.

This anchor is most relevant to three reviewer-facing hypotheses:

1. **Policy-as-Persistence**
2. **Trust-Graph Poisoning**
3. **Evidence-Suppression Objective**

These hypotheses are not conclusions.

They are validation targets for qualified DFIR, CTI, mobile forensic, platform-security, or OS-security review.

---

## 1. Policy-as-Persistence

### Relevance to this anchor

This repository focuses on restriction-layer behavior that appears without a clear visible management indicator.

The main question is whether policy state, restriction state, ScreenTime state, ManagedSettings behavior, Apple ID sign-out restriction behavior, or management-adjacent daemon activity could act as a persistence surface.

This does not require a classic malware payload to be visible.

### Reviewer question

> Is policy state acting as persistence, or can all observed restriction behavior be explained by normal Apple / iOS / iCloud / ScreenTime behavior?

### Relevant signal categories

* ScreenTime state
* Content & Privacy restriction behavior
* Apple ID sign-out restriction behavior
* ManagedSettings / FamilyControls traces
* management-adjacent daemon activity
* visible MDM / supervised / userIsManaged state mismatch
* repeated restriction-like behavior across device or account lineage

### What would support this hypothesis

* restriction behavior recurring without clear user configuration
* restriction behavior correlating with management-adjacent daemon activity
* restriction behavior persisting across restore, migration, Apple ID lineage, or device transitions
* mismatch between visible management state and effective restriction-like behavior

### What would weaken it

* confirmed local user configuration explaining the restriction behavior
* normal Apple / iOS / iCloud / ScreenTime behavior fully explaining the pattern
* no cross-device, cross-generation, or account-lineage continuity
* vendor-confirmed benign explanation for the relevant restriction-state transitions

---

## 2. Trust-Graph Poisoning

### Relevance to this anchor

The restriction event is not treated only as a local device issue.

It may reflect distortion of a broader trust graph involving Apple ID lineage, trusted-device behavior, account state, ScreenTime state, backup lineage, or authentication-related trust state.

### Reviewer question

> Is the trusted relationship itself being distorted across devices, accounts, backups, or authentication events?

### Relevant signal categories

* Apple ID lineage
* trusted devices
* device identity continuity
* usageClientId transitions
* backup lineage
* ScreenTime / restriction state continuity
* authentication or re-authentication events
* financial device-trust exposure, if present in the broader dataset

### What would support this hypothesis

* similar restriction or trust-state anomalies across multiple Apple devices
* continuity after device replacement, restore, or Apple ID migration
* repeated mismatch between visible management state and effective restriction behavior
* correlation between account / trust-state anomalies and authentication events

### What would weaken it

* all events explained by normal account migration, restore, or device replacement
* no cross-device or account-lineage continuity
* no relationship between restriction behavior and trust-state transitions
* clean platform-side confirmation that all trusted-device states were normal

---

## 3. Evidence-Suppression Objective

### Relevance to this anchor

The restriction layer may affect not only device usability, but also the user’s ability to preserve, export, explain, or validate evidence.

This does not prove malicious suppression.

It defines a review question: whether evidence-preservation behavior remained normal during important restriction-layer events.

### Reviewer question

> Did the system behave normally when the user attempted to preserve evidence?

### Relevant signal categories

* screenshot capture behavior
* screen recording behavior
* storage pressure during critical events
* backup inconsistency
* log preservation degradation
* artifact export difficulty
* restriction state interfering with user action
* timing correlation between evidence-preservation attempts and system degradation

### What would support this hypothesis

* preservation failures repeating during high-value events
* user evidence actions correlating with resource, daemon, restriction, or backup anomalies
* successful preservation on comparison devices under similar conditions
* failure modes aligning with the most important restriction-layer event windows

### What would weaken it

* preservation failures fully explained by storage exhaustion, user error, tool limitations, or ordinary iOS behavior
* no timing relationship to important restriction-layer events
* same failures reproduced on clean control devices
* no link between preservation failure and control-layer anomalies

---

## Boundary

This repository does not assert:

* malware attribution
* actor attribution
* state attribution
* Apple-side causation
* classic MDM enrollment
* known spyware family deployment
* confirmed C2
* confirmed payload
* confirmed exploit chain
* Evil Twin / rogue AP use as a proven fact

This anchor only asks whether invisible or support-adjacent restriction behavior should be treated as a meaningful control-layer signal for deeper review.

The preferred outcome is not confirmation.

The preferred outcome is a reproducible explanation that supports, weakens, or falsifies each hypothesis.
