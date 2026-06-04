# Support-Invisible Restriction-State Anchor: Public Technical Package

## Status

Public preliminary technical review package.

This repository is intended for qualified digital forensics, incident response, mobile forensic, legal-technical, or security research review.

It is not a public accusation.

It is not an attribution claim.

It is not a malware conclusion.

It is not a spyware-family claim.

It is not a claim against any vendor, country, group, product, service, mobile app vendor, telecom provider, backup tool, or individual.

This repository is a focused restriction-state anchor supporting the broader Shadow Cloud working hypothesis.

The current broader framing is:

Shadow Cloud is a non-attribution forensic model for mobile-native LOTL-like Apple platform-state anomalies.

This means the review target is not a named actor.

The review target is whether normal Apple / iOS / iCloud / iMazing / Microsoft-app behavior can explain the observed clustering of:

- trust state
- restriction state
- FileProvider state
- iCloud state
- ManagedSettings state
- account-calendar-document state
- evidence-preservation behavior

For this repository, the narrow question is not only whether a visible MDM profile exists.

The narrow question is:

Can restriction-like behavior surface through ScreenTime / ManagedSettings / DMD / Apple ID sign-out behavior while ordinary visible management indicators remain absent or false?

In short:

Traditional LOTL:
Living off tools.

Shadow Cloud:
Living off Apple platform state.

This repository is one support anchor.

It is not the final reduced DFRWS core set.

The broader DFRWS-normalized model retains two March-April 2026 core review lines in the main repository after Normal-Hypothesis Reduction.

This repository remains supporting material for the restriction-state / support-invisible policy-state portion of that broader model.

---

## Correction Notice

Earlier versions of this repository incorrectly treated 2026-03-03 as the Apple Support contact date.

Correction:

- 2026-03-03 is the preserved iOS artifact / sysdiagnose anchor date.
- 2026-03-04 is an additional anchor date involving Lost Mode, Find My, Game Center UI exposure, Visual Intelligence / ANE pressure, and Account / Cloud / Trust burst observations.
- 2026-03-05 is the Apple Support interaction date.
- The Apple Support interaction window was approximately 11:10-11:31 UTC+7 on 2026-03-05.
- The 2026-03-05 artifacts show ManagedSettings / Safari restriction changes around 11:11:38 UTC+7 and DMD / Digital Health / Game Center-related restriction recomputation shortly afterward.
- Later on 2026-03-05, screenshots/video reportedly captured Screen Time restriction UI and Apple ID sign-out restriction behavior.

This correction does not remove the artifact value of 2026-03-03.

It separates the case into three review dates:

1. 2026-03-03:
   FileProvider / MCState / ManagedSettings / visible-management-absent artifact anchor.

2. 2026-03-04:
   Lost Mode / Find My / Game Center exposure / ANE-VisualIntelligence pressure / Account-Cloud-Trust burst anchor.

3. 2026-03-05:
   Apple Support interaction plus ManagedSettings / DMD / Game Center recomputation plus later Screen Time UI evidence anchor.

---

## Public Repository Boundary

Raw iOS logs, raw sysdiagnose archives, raw screenshots, raw videos, private account data, Apple ID material, BSSID details, OTP / financial data, and sensitive backup artifacts are not included in this public repository.

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

Original raw artifacts are preserved separately.

They may be provided later through a qualified secure evidence-handling procedure if required by a qualified reviewer.

---

## Non-Attribution Boundary

This repository does not assert:

- confirmed malware
- confirmed payload
- confirmed C2
- confirmed exploit chain
- confirmed spyware-family deployment
- confirmed MDM enrollment
- confirmed supervision
- confirmed configuration profile proving management
- confirmed actor attribution
- confirmed state attribution
- confirmed government attribution
- confirmed vendor attribution
- confirmed Apple attribution
- confirmed iMazing attribution
- confirmed Microsoft attribution
- confirmed Outlook causation
- confirmed telecom compromise
- confirmed baseband compromise
- confirmed SIM compromise
- confirmed OTP interception
- confirmed attacker identity

Microsoft / Outlook / account-calendar-document surfaces, where mentioned, are possible future review surfaces or auxiliary correlative surfaces only.

They are not asserted as causes.

Subjective observations are not treated as standalone proof.

They may be used only as timestamp context for why the observer was interacting with, preserving, or reviewing the device.

The narrow purpose of this repository is to preserve and explain a support-invisible restriction-state anchor for technical review.

---

## Device Label

Internal label: 15G

Physical device class: iPhone 12 mini class device

Observed model identifier: iPhone13,1

Observed OS generation: iPhone OS 18.5 / 22F76

Important note:

15G is an internal Ghost / Apple ID lineage label.

It does not mean that the physical device is an iPhone 15 Pro.

---

## Core Technical Question

The core question is not whether classic visible MDM was installed.

The core question is whether the observed behavior can be explained by ordinary local Screen Time / Family Sharing / ManagedSettings behavior, or whether the artifacts show an account / cloud / policy-adjacent restriction state that was not visible as ordinary MDM, supervision, or configuration profile management.

Under the updated Shadow Cloud framing, this anchor should be read as a policy-state / restriction-state seam review package within the broader mobile-native LOTL-like Apple platform-state anomaly model.

The narrow technical question is:

Can a restriction-like state surface through ScreenTime / ManagedSettings / DMD / Apple ID sign-out behavior while ordinary visible management indicators remain absent?

The broader Shadow Cloud question is:

Can Apple platform state itself become the anomaly surface?

Reviewed artifact families include:

- MDMStatus:false
- IsSupervised:false
- PostSetupProfileWasInstalled:false
- empty visible profile / payload structures
- ManagedSettings / ScreenTime local stores
- DMD / Digital Health restriction recomputation
- FileProvider / SaveToFiles activity
- iCloud Drive shown as logged out / not configured in brctl
- FileProvider iCloud Drive provider state still present as enabled / needs-auth
- AppleAccount / CKKS / PCS / SOS / CloudServices / Networking bursts
- storage and memory-pressure context
- later visible Screen Time / sign-out restriction UI evidence on 2026-03-05

---

## Normal-Hypothesis Reduction

Ordinary explanations must be tested first.

The following are treated as normal-hypothesis candidates unless stronger cross-layer coupling remains:

- ordinary ScreenTime settings
- ordinary Family Sharing behavior
- ordinary Content & Privacy restrictions
- user-side configuration
- old or forgotten ScreenTime passcode state
- normal Game Center restriction behavior
- ordinary ManagedSettings behavior
- ordinary DMD / Digital Health recomputation
- ordinary iOS crash clustering
- ordinary account sign-in state
- ordinary iCloud state
- ordinary FileProvider behavior
- local device state
- isolated device failure
- storage pressure
- broad keyword hits
- weak temporal joins
- restriction artifacts without backup/evidence overlap
- restriction artifacts without account/cloud or telecom context

The purpose is not to prove a malicious explanation.

The purpose is to test whether normal Apple / iOS behavior can reproduce the full coupled structure.

---

## Anchor Summary

## 2026-03-03 - Artifact Anchor

The 2026-03-03 artifacts are treated as the first artifact anchor.

Key observations:

- MCState present
- IsSupervised:false
- PostSetupProfileWasInstalled:false
- visible profile / payload structures empty
- ManagedSettings / ScreenTime local stores present
- FileProvider / SaveToFiles activity present
- iCloud Drive shown as logged out / not configured in brctl
- FileProvider retained iCloud Drive provider state requiring authentication
- large fileproviderd disk-write activity
- storage and memory-pressure context
- no classic visible MDM indicator found in reviewed artifacts

This date is not the Apple Support contact date.

Review question:

Can ordinary Apple / iOS / iCloud / FileProvider / ManagedSettings behavior explain the visible-management absence plus restriction-adjacent artifact cluster?

---

## 2026-03-04 - Lost Mode / Game Center / Pressure Anchor

The 2026-03-04 artifacts are treated as an independent anchor, not merely a bridge day.

Key observations:

- Apple Pay stopped notification around 04:20 UTC+7
- Lost Mode enabled notification around 04:21 UTC+7
- screenshot/video evidence reportedly preserved around 04:20-04:50 UTC+7
- 04:43 UTC+7 Game Center UI screenshot reportedly captured
- Game Center social / friends-related restriction baseline still present in MCState around 05:13 UTC+7
- ANECompilerService large disk-write activity
- Visual Intelligence / Photos / Spotlight / media analysis concentration
- multiple 1GB-class disk-write events across ANECompilerService, WeChat, fileproviderd, and sysdiagnosed
- Wi-Fi disassociation / WWAN state context
- late-night physical-sensation report timestamp around 23:13 UTC+7
- around the same time, SFA / CloudServices / CKKS / PCS / SOS / Networking burst observed

Subjective physical observations are not treated as standalone proof of an external physical source.

They are used only as contemporaneous timestamp context for why the user was interacting with and observing the device.

Review question:

Can ordinary Lost Mode, Find My, Game Center, ANE / Visual Intelligence, FileProvider, storage-pressure, and account/cloud behavior explain this cluster?

---

## 2026-03-05 - Support-Window Anchor

The 2026-03-05 artifacts are treated as the Apple Support interaction anchor.

Key observations:

- Apple Support interaction window around 11:10-11:31 UTC+7
- ManagedSettings / Safari restriction changes around 11:11:38 UTC+7
- DMD / Digital Health restriction recomputation shortly afterward
- Game Center social / friends-related restriction recomputation around 11:14 UTC+7
- Apple Support-side confirmation reportedly indicated no ordinary visible Screen Time / Family Sharing / MDM / supervision configuration matching the observed restriction state
- 18:11 UTC+7 screenshot reportedly captured Screen Time restriction-related UI
- 18:12 UTC+7 video reportedly captured Screen Time settings and Apple ID sign-out restriction behavior
- WeChat large disk-write pressure later the same day
- no classic visible MDM / supervision / profile indicator found in reviewed artifacts

Review question:

Can ordinary ScreenTime, Family Sharing, ManagedSettings, DMD / Digital Health, Game Center, Apple Support visibility, and local device settings explain the support-window sequence?

---

## Cross-Day Interpretation

The three dates should be read together.

2026-03-03:

- artifact-level visible-management absence
- FileProvider / ManagedSettings / storage-pressure context

2026-03-04:

- Lost Mode / Find My / Game Center exposure
- ANE / Visual Intelligence / storage-pressure context
- Account / Cloud / Trust burst context

2026-03-05:

- Apple Support window
- ManagedSettings / DMD / Game Center restriction recomputation
- later visible Screen Time / sign-out restriction UI evidence

Together, the observations support a technical review question:

Can an account / cloud / policy-adjacent restriction state exist or persist without ordinary visible MDM, supervision, or configuration profile indicators, and later surface through Screen Time / ManagedSettings / Apple ID sign-out restriction behavior?

This is a review question.

It is not a conclusion.

---

## Relationship to Main Shadow Cloud Repository

This repository is a focused support anchor package.

It should be read as supporting material for the broader Shadow Cloud model, not as a standalone conclusion.

The broader model asks whether normal Apple / iOS / iCloud / iMazing / Microsoft-app behavior can explain a long-term, cross-device structure involving:

- trust state
- restriction state
- management-adjacent daemon state
- backup state
- account-calendar-document state
- telecom context
- proximity context
- evidence-preservation behavior

This repository focuses only on the restriction-state and support-invisible policy-state portion of that broader model.

---

## Relationship to DFRWS-Normalized Core Lines

The broader DFRWS-normalized Shadow Cloud model retains two March-April 2026 core review lines after Normal-Hypothesis Reduction:

1. 2026-03-15 to 2026-03-21
   Centered on 2026-03-17 to 2026-03-19

2. 2026-03-29 to 2026-04-04
   Centered on 2026-03-31 to 2026-04-02

This support repository is not the final reduced core set.

It is an earlier and narrower restriction-state anchor that supports the restriction-state / support-invisible policy-state branch of the broader model.

The value of this repository is not that it proves Shadow Cloud.

The value is that it preserves a focused review sequence for testing whether restriction-like behavior can surface while ordinary visible management indicators remain absent.

---

## Relationship to MDMStatus:false

MDMStatus:false is not treated as proof of hidden management.

The review question is narrower:

Can MDMStatus:false, IsSupervised:false, visible-management absence, restriction-related services, and management-adjacent artifact context coexist normally under the reviewed conditions?

This repository does not claim:

- confirmed MDM enrollment
- confirmed supervision
- configuration profile proving management
- hidden MDM as a conclusion

The issue is a restriction-state review question.

---

## Relationship to FileProvider / iCloud State

FileProvider and iCloud Drive state are relevant because they may connect account/cloud state, document-provider state, and evidence-preservation behavior.

Relevant surfaces include:

- FileProvider
- iCloud Drive provider state
- SaveToFiles / fileproviderd activity
- provider authentication state
- iCloud logged-out versus provider-needs-auth context
- storage pressure

This repository does not claim FileProvider compromise.

The review question is whether ordinary FileProvider / iCloud behavior explains the timing and coupling with restriction-state artifacts.

---

## Relationship to Microsoft / Outlook

Microsoft / Outlook surfaces are not central to this repository.

Where mentioned, they are possible future review surfaces or auxiliary correlative surfaces only.

This repository does not claim:

- Microsoft attribution
- Outlook causation
- Microsoft app causation
- Microsoft service causation
- Microsoft mobile apps directly modified Manifest.db
- Microsoft mobile apps directly modified Apple backup state
- Microsoft mobile apps directly modified iOS backup services
- Microsoft surfaces caused restriction-state behavior

The safe interpretation is:

Microsoft / Outlook surfaces, if later reviewed in preserved artifacts, should be evaluated as possible account-calendar-document-policy surfaces, not assumed causes.

---

## Strengthening Conditions

This support-invisible restriction-state anchor is strengthened if qualified review shows that:

- ordinary ScreenTime settings do not explain the reviewed behavior
- Family Sharing does not explain the reviewed behavior
- user configuration does not explain the reviewed behavior
- Apple Support visibility does not match local restriction-state behavior under ordinary conditions
- MDMStatus:false / IsSupervised:false / visible-management absence conflicts with restriction-like behavior
- ManagedSettings / DMD / Digital Health recomputation aligns with user-visible restriction behavior
- Game Center restriction behavior aligns with ScreenTime / ManagedSettings state
- FileProvider / iCloud state aligns with restriction-state timing
- storage pressure or evidence-preservation difficulty aligns with the same sequence
- clean controls do not reproduce the same structure

---

## Weakening or Falsification Conditions

This support-invisible restriction-state anchor is weakened if qualified review shows that:

- ordinary ScreenTime settings explain the pattern
- Family Sharing explains the restriction behavior
- local user configuration explains the observed state
- old or forgotten ScreenTime passcode state explains the sequence
- Apple Support visibility can normally differ from local device state in this exact way
- ManagedSettings behavior is ordinary and unrelated
- DMD / Digital Health recomputation is ordinary and unrelated
- Game Center behavior is ordinary and unrelated
- FileProvider behavior is ordinary and unrelated
- storage pressure explains the preservation difficulty
- restriction-state timing does not align with other platform-state seams
- clean controls reproduce the same structure
- subjective observations are the only remaining support

If these conditions are met, this restriction-state anchor should be weakened or rejected.

---

## Reviewer Questions

A qualified reviewer should ask:

1. Can ordinary ScreenTime settings explain the reviewed restriction behavior?
2. Can Family Sharing explain the reviewed restriction behavior?
3. Can local user configuration or old ScreenTime passcode state explain the sequence?
4. Can ManagedSettings / DMD / Digital Health recomputation explain the pattern under ordinary iOS behavior?
5. Can MDMStatus:false / IsSupervised:false normally coexist with the reviewed restriction-state artifacts?
6. Can visible-management absence coexist with the observed restriction-like behavior under normal conditions?
7. Can Apple ID sign-out restriction behavior be explained by ordinary settings?
8. Can Game Center restriction behavior be explained by ordinary settings?
9. Can Apple Support-side visibility differ from local device restriction state in this way under normal conditions?
10. Does restriction-state timing align with FileProvider or iCloud state?
11. Does restriction-state timing align with storage pressure or evidence-preservation difficulty?
12. Can clean controls reproduce the same restriction-state sequence?
13. If normal explanations reproduce the structure, what documented test demonstrates it?
14. If normal explanations do not reproduce the structure, does this support-invisible restriction-state anchor justify deeper mobile forensic review?

---

## Practical Takeaway

This repository does not ask reviewers to accept the Shadow Cloud hypothesis.

It asks reviewers to test whether a support-invisible restriction-state pattern can be reproduced through normal Apple / iOS / iCloud behavior.

The final position is:

Restriction-state artifacts are review targets, not conclusions.

MDMStatus:false does not prove hidden management.

Visible-management absence plus restriction-like behavior is a review question.

Subjective observations are timestamp context only, not standalone proof.

This repository is a supporting restriction-state anchor, not the final reduced core set.

If normal behavior explains the sequence, this anchor should be weakened.

If normal behavior does not explain the sequence, this repository may represent a focused policy-state / restriction-state seam requiring deeper mobile forensic review.
