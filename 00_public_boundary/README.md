# Public Boundary

## Purpose

This directory defines the public boundary of this repository.

It explains:

* what this public package is
* what it is not
* the correction from the earlier 2026-03-03-only framing
* the device label used in this repository
* the scope requested from qualified reviewers

---

## Public package status

This repository is a public technical review package.

It is intended to help qualified reviewers understand the structure of the preserved artifacts without exposing raw sensitive data.

The repository contains summaries, timelines, artifact names, script references, and review questions.

It does not contain raw logs, raw sysdiagnose archives, raw screenshots, or raw videos.

---

## Key correction

Earlier versions incorrectly treated 2026-03-03 as the Apple Support contact date.

Correct structure:

* 2026-03-03: artifact / FileProvider / MCState / ManagedSettings anchor
* 2026-03-04: Lost Mode / Find My / Game Center / ANE-VisualIntelligence / Account-Cloud-Trust burst anchor
* 2026-03-05: Apple Support interaction / ManagedSettings-DMD-Game Center recomputation / later Screen Time UI evidence anchor

This repository now uses the three-anchor structure.

---

## Public boundary

The public repository may include:

* artifact names
* log titles
* sysdiagnose archive names
* dates and approximate times
* technical summaries
* process names
* subsystem names
* interpretation boundaries
* SHA256 references where available
* private evidence index IDs
* reproducibility scripts

The public repository must not include:

* raw iOS log archives
* raw sysdiagnose archives
* raw screenshots
* raw videos
* full Apple Support screenshots
* Apple ID identifiers
* phone numbers
* precise location data
* full BSSID / SSID lists
* nearby-device identifiers
* private contact data
* financial account data

---

## Review posture

The package should be read as a structured technical question.

It does not claim attribution.

It does not claim malware proof.

It does not claim that Evil Twin, Rogue AP, malicious profile injection, Pegasus, or any named APT group has been proven.

The intended review is:

1. Validate the timeline.
2. Validate the artifact interpretation.
3. Compare ordinary iOS behavior against anomalous behavior.
4. Determine whether the observed Screen Time / ManagedSettings / Apple ID sign-out restriction state can be explained by ordinary visible Screen Time, Family Sharing, MDM, or supervision state.
5. Identify which raw artifacts would be needed for private verification.

---

## Directory contents

* `correction_notice.md`
  Explains the correction from the earlier 2026-03-03-only framing.

* `device_label_15G.md`
  Defines the internal device label used in this repository.

* `reviewer_scope.md`
  Defines what reviewers are asked to evaluate.

---

## Important note

Subjective observations are not treated as standalone proof.

They are included only when they provide contemporaneous timestamp context for device interaction, screenshot capture, Apple Support contact, or artifact generation.

The technical review should prioritize device artifacts, timestamps, logs, sysdiagnose extracts, UI evidence, and reproducible script output.
