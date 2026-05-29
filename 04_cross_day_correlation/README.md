# Cross-Day Correlation

## Purpose

This directory summarizes the cross-day relationship between the three anchor dates:

* `2026-03-03`
* `2026-03-04`
* `2026-03-05`

The purpose is to show how the observations connect across multiple days, instead of treating each date as an isolated event.

---

## Cross-day structure

The corrected structure is:

### 2026-03-03

`FileProvider / MCState / ManagedSettings / visible-management-absent artifact anchor`

Primary role:

* baseline artifact state
* visible management absence
* MCState / ManagedSettings presence
* FileProvider / iCloud Drive needs-auth context
* large fileproviderd disk-write pressure

---

### 2026-03-04

`Lost Mode / Find My / Game Center exposure / ANE-VisualIntelligence pressure / Account-Cloud-Trust burst anchor`

Primary role:

* Lost Mode / Apple Pay stopped timestamp context
* Find My / Family / AppleAccount context
* Game Center UI exposure
* Game Center restriction baseline
* multiple 1GB-class disk-write events
* late-night Account / Cloud / Trust burst context

---

### 2026-03-05

`Apple Support interaction / ManagedSettings-DMD-Game Center recomputation / later Screen Time UI evidence anchor`

Primary role:

* Apple Support interaction window
* ManagedSettings / Safari restriction change
* DMD / Digital Health recomputation
* Game Center social restriction recomputation
* later Screen Time / Apple ID sign-out restriction UI evidence
* WeChat storage-pressure context

---

## Main cross-day observation

The main observation is not a single isolated log.

The main observation is a sequence:

1. Visible management indicators were absent.
2. Internal restriction-related structures were present.
3. FileProvider / iCloud Drive / account-cloud context persisted.
4. Lost Mode / Find My / Game Center UI context appeared.
5. Game Center social restriction baseline existed before the Apple Support date.
6. Apple Support interaction occurred.
7. ManagedSettings / DMD / Game Center recomputation occurred in the same support-window range.
8. Later Screen Time / Apple ID sign-out restriction UI evidence was captured.
9. Large disk-write / storage-pressure events repeated across the three dates.

---

## Why the sequence matters

The three dates create a stronger review question than any single date alone.

### If reviewed alone

* 2026-03-03 may look like FileProvider / low-storage behavior.
* 2026-03-04 may look like Lost Mode / Photos / ANE / diagnostic pressure.
* 2026-03-05 may look like ordinary Screen Time or account configuration.

### When reviewed together

The pattern becomes more specific:

* visible MDM / supervision / profile indicators remain absent
* ManagedSettings / DMD / Digital Health structures are present or change
* Game Center social restrictions appear as a cross-day seam
* FileProvider / iCloud Drive needs-auth context recurs
* AppleAccount / CKKS / CloudServices / PCS / SOS context recurs
* user-side UI evidence aligns with device-side state changes
* storage pressure repeats across different processes

---

## Normal interpretation

A normal interpretation may be:

* low storage caused repeated disk-write pressure
* iOS background indexing caused Photos / Visual Intelligence / Spotlight activity
* Lost Mode caused ordinary Find My / Apple Pay / account behavior
* Screen Time / ManagedSettings recomputation was ordinary system behavior
* Game Center restriction keys were normal template keys
* Apple Support timing was coincidental
* later Screen Time UI evidence reflected normal user/account configuration

---

## Anomalous interpretation

An anomalous interpretation may be:

* visible MDM / supervision / profile indicators were absent, but internal restriction layers persisted
* FileProvider / iCloud Drive needs-auth state and `brctl` not-configured state showed an account/trust-state edge case
* Game Center appeared as an exposed seam in a broader restriction template
* Apple Support timing aligned with ManagedSettings / DMD / Game Center recomputation
* later Screen Time / Apple ID sign-out restriction UI evidence appeared after the internal recomputation window
* repeated 1GB-class disk-write pressure may have affected evidence preservation or device-state observation

---

## TTP hypothesis boundary

This repository includes TTP comparison only as a review aid.

Comparison models include:

* Evil Twin / Rogue AP style physical-proximity Wi-Fi techniques
* account / trust-state manipulation hypotheses
* APT42-like cloud/account-control workflow
* APT32-related historical TTP comparison
* support/account workflow manipulation
* user-interaction-gated control models

These are comparison models.

They are not attribution claims.

---

## Files in this directory

* `2026-03-03_vs_2026-03-04_vs_2026-03-05.md`
  Three-day comparison table and timeline logic.

* `visible_management_absent_internal_restriction_present.md`
  Visible-management absence vs internal restriction-layer presence.

* `storage_pressure_comparison.md`
  Cross-day disk-write and pressure comparison.

* `ttp_comparison_hypothesis.md`
  TTP comparison hypothesis, including Evil Twin-like physical-proximity Wi-Fi TTP and APT42-like account/cloud-control model.

---

## Boundary

This directory does not prove:

* malware
* actor attribution
* Evil Twin / Rogue AP use
* malicious profile injection
* classic MDM enrollment
* Apple-side causation
* that Apple Support caused the restriction events
* that Game Center was the main target

This directory only explains why the three dates should be reviewed together.
