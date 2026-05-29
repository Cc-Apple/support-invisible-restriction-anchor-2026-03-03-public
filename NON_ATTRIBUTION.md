# Non-Attribution Statement

## Purpose

This repository is a public technical review package.

It is intended to preserve and organize observations related to iOS artifacts, Apple account state, Screen Time / ManagedSettings behavior, FileProvider activity, AppleAccount / CKKS / CloudServices signals, and related timeline anchors.

This repository is not an attribution report.

---

## No actor attribution

This repository does not attribute the observed behavior to:

* Apple
* any Apple employee
* any government
* any intelligence agency
* any law-enforcement body
* any private surveillance vendor
* any known APT group
* any unknown APT group
* any named individual
* any specific country
* any specific organization

Any references to APT32, APT42, APT28, APT41, APT10, APT27, Pegasus, NSO Group, Evil Twin, Rogue AP, or similar public terms are used only as TTP comparison models.

They are not claims of responsibility.

---

## No malware conclusion

This repository does not claim that malware was found.

It does not claim that:

* a specific exploit was used
* a specific zero-day was used
* a specific spyware family was used
* Pegasus or any Pegasus-like spyware was used
* an APT group directly compromised the device
* Apple intentionally performed the observed actions
* a malicious configuration profile was proven
* Evil Twin / Rogue AP activity was proven
* MDM enrollment was proven

The reviewed artifacts repeatedly show the opposite of classic visible MDM indicators:

* `MDMStatus:false`
* `IsSupervised:false`
* `PostSetupProfileWasInstalled:false`
* empty visible profile / payload structures

The question is therefore not whether classic visible MDM was found.

The question is whether the observed restriction behavior can be explained by ordinary iOS behavior, or whether it indicates an account/cloud/policy-adjacent restriction state that is not visible as ordinary MDM, supervision, or configuration profile management.

---

## TTP comparison boundary

This repository includes limited TTP comparison only to help qualified reviewers frame technical questions.

The current comparison model is:

Physical-proximity-seeded account / trust-state manipulation
plus
user-interaction-gated cloud/account-control workflow
plus
visible-management-absent internal restriction layer exposure.

This model is only a hypothesis.

It is not an attribution claim.

It is not a conclusion.

---

## Subjective observations

Some timeline notes include subjective observations, such as physical sensations, environmental sounds, nearby-device behavior, or perceived proximity events.

These are not treated as standalone proof of an external cause.

They are included only when they provide contemporaneous timestamp context for why the user interacted with the device, captured screenshots, contacted Apple Support, or generated relevant artifacts.

The technical review should prioritize:

* device logs
* sysdiagnose artifacts
* MCState / ManagedSettings evidence
* AppleAccount / CKKS / CloudServices records
* FileProvider and storage-pressure records
* screenshot/video timestamps
* Apple Support interaction timestamps
* reproducible script outputs

---

## Reviewer position

Reviewers should treat this repository as a structured question set, not as a conclusion.

The requested review is:

1. Validate the timestamps.
2. Validate the artifact interpretations.
3. Separate ordinary iOS behavior from anomalous behavior.
4. Confirm or reject the ManagedSettings / DMD / Digital Health interpretation.
5. Confirm or reject the FileProvider / iCloud Drive / AppleAccount trust-state interpretation.
6. Determine whether the later Screen Time / Apple ID sign-out restriction UI evidence can be explained by ordinary visible Screen Time, Family Sharing, MDM, or supervision state.

No attribution conclusion should be drawn from this public package alone.
