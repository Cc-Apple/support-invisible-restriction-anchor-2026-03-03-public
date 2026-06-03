# Support Invisible Restriction Anchor - Public Technical Package

## Status

Public preliminary technical review package.

This repository is intended for qualified digital forensics, incident response, mobile forensic, legal-technical, or security research review.

It is not a public accusation, attribution claim, malware conclusion, spyware-family claim, or claim against any vendor, country, group, product, service, or individual.

This repository is a focused technical anchor supporting the broader **Shadow Cloud** working hypothesis.

The current recommended broader framing is:

> Shadow Cloud is a non-attribution, mobile-native LOTL-like Apple platform-state anomaly hypothesis.

This means the review target is not a named actor.

The review target is whether normal Apple / iOS / iCloud / iMazing / Microsoft-app behavior can explain the observed clustering of trust state, restriction state, FileProvider state, iCloud state, ManagedSettings state, account-calendar-document state, and evidence-preservation behavior.

For this repository, that means the reviewed question is not only whether a visible MDM profile exists.

The reviewed question is whether Apple platform state, restriction state, trust state, FileProvider state, iCloud state, ManagedSettings state, and evidence-preservation behavior appear to cluster in a way that normal Apple / iOS behavior can explain.

In short:

> Not living off tools.
> Living off Apple platform state.

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

This correction does not remove the artifact value of 2026-03-03.

It separates the case into three review dates:

1. 2026-03-03: FileProvider / MCState / ManagedSettings / visible-management-absent artifact anchor.
2. 2026-03-04: Lost Mode / Find My / Game Center exposure / ANE-VisualIntelligence pressure / Account-Cloud-Trust burst anchor.
3. 2026-03-05: Apple Support interaction + ManagedSettings / DMD / Game Center recomputation + later Screen Time UI evidence anchor.

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

## Non-attribution boundary

This repository does not assert:

* confirmed malware
* confirmed payload
* confirmed C2
* confirmed exploit chain
* confirmed spyware-family deployment
* confirmed MDM enrollment
* confirmed actor attribution
* confirmed state attribution
* confirmed government attribution
* confirmed vendor attribution
* confirmed Apple attribution
* confirmed iMazing attribution
* confirmed Microsoft attribution
* confirmed Outlook causation
* confirmed telecom compromise
* confirmed baseband compromise
* confirmed SIM compromise
* confirmed OTP interception
* confirmed attacker identity

Microsoft / Outlook / account-calendar-document surfaces, where mentioned, are possible future review surfaces only.

They are not asserted as causes.

The narrow purpose of this repository is to preserve and explain a support-invisible restriction-state anchor for technical review.

---

## Device label

Internal label: `15G`

Physical device class: iPhone 12 mini class device

Observed model identifier: `iPhone13,1`

Observed OS generation: iPhone OS 18.5 / 22F76

Important note:

`15G` is an internal Ghost / Apple ID lineage label.

It does not mean that the physical device is an iPhone 15 Pro.

---

## Core technical question

The core question is not whether classic visible MDM was installed.

The key question is whether the observed behavior can be explained by ordinary local Screen Time / Family Sharing / ManagedSettings behavior, or whether the artifacts show an account / cloud / policy-adjacent restriction state that was not visible as ordinary MDM, supervision, or configuration profile management.

Under the updated Shadow Cloud framing, this anchor should be read as a **policy-state / restriction-state seam review package** within the broader mobile-native LOTL-like Apple platform-state anomaly model.

The narrow technical question is:

> Can a restriction-like state surface through ScreenTime / ManagedSettings / DMD / Apple ID sign-out behavior while ordinary visible management indicators remain absent?

The broader Shadow Cloud question is:

> Can Apple platform state itself become the anomaly surface?

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

Subjective physical observations are not treated as standalone proof of an external physical source.

They are used only as contemporaneous timestamp context for why the user was interacting with and observing the device.

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

> Can an account / cloud / policy-adjacent restriction state exist or persist without ordinary visible MDM, supervision, or configuration profile indicators, and later surface through Screen Time / ManagedSettings / Apple ID sign-out restriction behavior?

---

## Relationship to the main Shadow Cloud repository

This repository is a focused anchor package.

It should be read as supporting material for the broader Shadow Cloud model, not as a standalone conclusion.

The broader model asks whether normal Apple / iOS / iCloud / iMazing / Microsoft-app behavior can explain a long-term, cross-device structure involving:

* trust state
* restriction state
* management-adjacent daemon state
* backup state
* account-calendar-document state
* telecom context
* proximity context
* evidence-preservation behavior

This repository focuses only on the restriction-state and support-invisible policy-state portion of that broader model.

---

## Reviewer questions

A qualified reviewer should ask:

1. Can the observed restriction-like behavior be fully explained by ordinary Screen Time, Family Sharing, or local user configuration?
2. Can `MDMStatus:false`, `IsSupervised:false`, and empty visible profile / payload structures normally coexist with the reviewed restriction-state artifacts?
3. Can ManagedSettings / DMD / Digital Health / Game Center recomputation explain the observed UI behavior without deeper account or policy-state review?
4. Can FileProvider / iCloud Drive needs-auth state explain the artifact cluster?
5. Can Apple Support-side visibility differ from local device restriction state in this way under normal conditions?
6. Can storage pressure and disk-write events explain the evidence-preservation difficulty?
7. Does the 2026-03-03 / 2026-03-04 / 2026-03-05 sequence reflect normal Apple / iOS behavior, or does it remain a policy-state / restriction-state seam requiring deeper review?

---

## Practical takeaway

This repository does not ask reviewers to accept the Shadow Cloud hypothesis.

It asks reviewers to test whether a support-invisible restriction-state pattern can be reproduced through normal Apple / iOS / iCloud behavior.

If normal behavior explains the sequence, the hypothesis should be weakened.

If normal behavior does not explain the sequence, this repository may represent a focused policy-state / restriction-state seam requiring deeper mobile forensic review.
