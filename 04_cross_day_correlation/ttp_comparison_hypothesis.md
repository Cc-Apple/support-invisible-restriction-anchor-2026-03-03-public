# TTP Comparison Hypothesis

## Purpose

This file defines the public TTP comparison hypothesis used in this repository.

This is not an attribution claim.

This file compares the observed seam failures with public TTP models only to help qualified reviewers frame the technical questions.

---

## Non-attribution boundary

This repository does not attribute the observed behavior to:

* APT32
* APT42
* APT28
* APT41
* APT10
* APT27
* Pegasus
* NSO Group
* Apple
* any government
* any country
* any private vendor
* any named individual

Any group or technique names in this file are comparison models only.

They are not claims of responsibility.

---

## Working comparison model

The current working comparison model is:

```text
Physical-proximity-seeded account / trust-state manipulation
+
user-interaction-gated cloud/account-control workflow
+
visible-management-absent internal restriction-layer exposure
```

Short form:

```text
Physical-proximity seed
→ account / trust-state transition
→ cloud/account-control workflow
→ internal restriction-layer recomputation
→ later visible Screen Time / sign-out restriction UI
```

---

## Why a TTP comparison is used

The reviewed artifacts do not currently prove:

* a specific malware family
* a specific exploit
* Evil Twin / Rogue AP use
* malicious profile injection
* classic MDM enrollment
* a specific APT actor

However, the artifacts show seam behavior that benefits from TTP-level comparison.

Relevant seam observations include:

* visible MDM / supervision / profile indicators absent
* MCState / ManagedSettings present
* DMD / Digital Health recomputation
* Game Center social restriction recomputation
* Apple Support interaction window alignment
* FileProvider / iCloud Drive needs-auth context
* AppleAccount / CKKS / PCS / SOS / CloudServices context
* repeated 1GB-class storage-pressure events
* user-interaction windows aligned with device-side artifact bursts

---

## Layer 1: physical-proximity Wi-Fi TTP comparison

Comparison model:

```text
Evil Twin / Rogue AP style physical-proximity Wi-Fi TTP
```

This is a technique category, not an actor name.

Relevant comparison points:

* physical proximity may be required
* Wi-Fi / BSSID / RSSI / SSID context can become important
* user interaction may be required
* route changes between Wi-Fi and cellular / WWAN may become relevant
* credential capture, captive portal, or trust-state manipulation are possible review questions

Current evidence boundary:

This repository does not prove Evil Twin or Rogue AP use.

It only treats physical-proximity Wi-Fi techniques as a comparison model.

---

## Layer 2: cloud/account-control workflow comparison

Comparison model:

```text
APT42-like cloud/account-control objective
```

This refers to a style of operation, not actor attribution.

Relevant comparison points:

* cloud accounts
* identity state
* support / account workflows
* social engineering
* user interaction
* long-term account monitoring
* credential or trust-state dependency

Current evidence boundary:

This repository does not claim APT42 involvement.

It only uses APT42-like behavior as a comparison for cloud/account-centric control logic.

---

## Layer 3: regional / historical TTP comparison

Comparison model:

```text
APT32-adjacent historical TTP comparison
```

This refers to historical and regional TTP comparison only.

Relevant comparison points:

* long-term targeted operations
* Southeast Asia relevance
* credential / web / account-oriented operations
* strategic compromise style
* stealthy persistence and staged activity

Current evidence boundary:

This repository does not claim APT32 involvement.

APT32 is relevant only as a historical comparison model for how a regional actor’s older TTPs might fail or expose seams if combined with a newer account/cloud-control objective.

---

## Handcraft mismatch hypothesis

The core hypothesis is not that one known group exactly matches the artifacts.

The core hypothesis is that the seam failures may appear when different operational layers are combined:

```text
Older physical-access or Wi-Fi-access technique
+
newer cloud/account-control objective
+
Apple account / Screen Time / ManagedSettings / DMD restriction layer
```

Potential seam failures:

* visible MDM indicators remain absent
* internal restriction keys still change
* Game Center social restriction keys appear unexpectedly
* iCloud Drive appears not configured in one layer but needs-auth in FileProvider
* Apple Support window aligns with restriction recomputation
* low-use UI areas expose internal restriction template behavior
* storage pressure appears during evidence-generation or observation windows

---

## APT32 + Evil Twin + APT42-like model

A reviewer-facing way to describe the hybrid hypothesis:

```text
APT32-related historical TTP comparison
+
Evil Twin-like physical-proximity Wi-Fi access technique
+
APT42-like cloud/account-control objective
```

Meaning:

* APT32 is not claimed as the actor.
* Evil Twin is not claimed as proven.
* APT42 is not claimed as the actor.
* The model is used only to compare whether old access methods and modern cloud/account objectives could create the observed seam failures.

---

## Why Game Center matters in the TTP model

Game Center is treated as a seam, not as the target.

Relevant sequence:

1. 2026-03-04:

   * Game Center UI exposure reportedly captured.
   * Game Center social restriction baseline still present.

2. 2026-03-05:

   * Game Center social / friends-related restriction recomputation appeared around the Apple Support window.

Interpretation:

If a restriction template is being recomputed broadly, a low-use surface like Game Center may expose behavior that would otherwise remain unnoticed.

Review question:

Is Game Center recomputation ordinary Digital Health / Screen Time behavior, or does it reveal a broader internal restriction template being modified?

---

## Why Apple Support timing matters in the TTP model

The Apple Support window is important because it may represent a user-interaction-gated workflow.

Relevant sequence:

1. User contacts Apple Support around `2026-03-05 11:10-11:31 UTC+7`.
2. ManagedSettings / Safari restriction change appears around `11:11:38 UTC+7`.
3. DMD / Digital Health / Game Center recomputation appears shortly afterward.
4. Later UI evidence reportedly shows Screen Time and Apple ID sign-out restriction behavior.

Possible interpretation:

The support window may be an ordinary coincidence.

Alternative review question:

Did user interaction, account-state checking, or support workflow trigger or reveal an internal restriction-state transition?

---

## Why storage pressure matters in the TTP model

Repeated storage-pressure events matter because they may affect:

* screenshot preservation
* video capture
* log writing
* app stability
* sysdiagnose behavior
* FileProvider behavior
* user observation and reporting

Cross-day pressure pattern:

* 2026-03-03: fileproviderd
* 2026-03-04: ANECompilerService / WeChat / fileproviderd / sysdiagnosed
* 2026-03-05: WeChat

This does not prove intentional suppression.

It creates a review question:

Were these ordinary low-storage events, or did they form a repeated pressure pattern that affected evidence preservation and device-state observation?

---

## Normal interpretation

A normal interpretation may be:

* no actor model is needed
* no TTP model is needed
* all events are explainable by normal iOS behavior
* low storage caused repeated write pressure
* Lost Mode caused ordinary Apple Pay / Find My changes
* Game Center restriction keys are ordinary template keys
* Apple Support timing was coincidental
* ManagedSettings / DMD recomputation was normal maintenance
* later Screen Time UI evidence reflects ordinary local settings

---

## Anomalous interpretation

An anomalous interpretation may be:

* ordinary visible management indicators were absent
* internal restriction layers were present and later recomputed
* Game Center appeared as an exposed seam
* account/cloud/trust-state bursts appeared near key user-interaction windows
* storage pressure repeatedly appeared during observation or evidence windows
* Apple Support timing aligned with ManagedSettings / DMD / Game Center recomputation
* a hybrid TTP model may better explain the seams than a single isolated iOS bug

---

## Review questions

Qualified reviewers should evaluate:

1. Are physical-proximity Wi-Fi TTPs technically relevant to the observed route / BSSID / user-interaction concerns?
2. Does the observed sequence fit any known account/cloud-control workflow model?
3. Are APT32, APT42, or other APT references useful only as comparison models, or should they be removed entirely?
4. Is Game Center recomputation ordinary in this context?
5. Can visible-management absence coexist with later Screen Time / sign-out restriction UI in ordinary iOS behavior?
6. Are repeated pressure events better explained by low storage or by a cross-day device-state pattern?
7. What raw artifacts would be needed to test the Evil Twin / Rogue AP hypothesis?
8. What Apple-side records would be needed to test the account / trust-state hypothesis?

---

## Boundary

This file does not prove:

* APT32 involvement
* APT42 involvement
* APT28 involvement
* APT41 / APT10 / APT27 involvement
* Evil Twin / Rogue AP use
* malicious profile injection
* classic MDM enrollment
* malware
* Apple-side causation
* state actor involvement

This file only provides a structured TTP comparison hypothesis for qualified review.
