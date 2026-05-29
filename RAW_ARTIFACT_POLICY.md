# Raw Artifact Policy

## Purpose

This repository is a public technical review package.

Raw artifacts are not included in this public repository.

This policy explains what is excluded, why it is excluded, and how raw artifacts are preserved for qualified review.

---

## Raw artifacts are not public

This public repository does not include:

* raw iOS log ZIP archives
* raw sysdiagnose archives
* raw `.ips` files
* raw `.ips.ca.synced` files
* raw `.session` files
* raw `.spin` files
* raw `.plist` dumps
* raw screenshots
* raw videos
* raw Apple Support screenshots
* raw Apple ID / iCloud / Family Sharing screenshots
* raw Screen Time screenshots
* raw Find My screenshots
* raw network identifiers such as BSSID / SSID / precise location metadata
* raw device identifiers
* raw personal account identifiers
* raw phone numbers
* raw contact records

Only summaries, referenced artifact names, timestamps, SHA256 references where available, and review-oriented extracts are included.

---

## Reason for exclusion

Raw artifacts may contain sensitive information, including:

* Apple ID-related data
* device identifiers
* account state information
* location information
* network identifiers
* nearby Wi-Fi / Bluetooth information
* personal screenshots
* private messages
* contact information
* application usage records
* financial app context
* Apple Support case context

Publishing those artifacts directly would create unnecessary privacy and security risk.

---

## Preservation status

The original raw artifacts are preserved separately.

They include, where available:

* original log ZIP archives
* sysdiagnose archives
* screenshots
* videos
* Apple Support-related records
* SHA256 reference material
* local analysis outputs
* extracted summaries

Raw artifacts may be provided only through a controlled review process if a qualified reviewer requires them.

---

## Public evidence model

This repository uses a reference-based evidence model.

Each public summary should identify:

* date
* local time zone
* artifact category
* log title or sysdiagnose archive name
* observed process or subsystem
* relevant timestamp
* interpretation boundary
* normal interpretation
* anomalous interpretation
* SHA256 reference where available

The public repository should not expose raw sensitive data unless explicitly redacted.

---

## Reviewer access

A qualified reviewer may request raw artifacts for private verification.

Before sharing raw artifacts, the reviewer should specify:

1. Which artifact is needed.
2. Why the public summary is insufficient.
3. Whether only a redacted extract is enough.
4. Whether SHA256 verification is required.
5. How the artifact will be stored and protected.

Raw artifacts should not be posted publicly as part of routine repository updates.

---

## Network and location data

Network and location-sensitive data must be treated carefully.

The public repository should not publish:

* full BSSID values
* precise GPS coordinates
* exact home address or nearby address strings
* precise Wi-Fi scan lists
* nearby-device identifiers
* Bluetooth identifiers

If relevant, these should be summarized as:

* Wi-Fi connected / not connected
* WWAN / cellular route active
* BSSID present but redacted
* RSSI range only
* nearby scan observed but not published
* location evidence preserved privately

---

## Screenshot and video evidence

Screenshots and videos are preserved privately.

Public summaries may reference screenshot/video evidence by:

* date
* approximate time
* visible UI category
* reason for relevance
* private evidence index ID

Example:

`2026-03-05 18:12 VN - private video evidence reportedly captures Screen Time settings and Apple ID sign-out restriction UI. Raw video is not public.`

The public repository should avoid publishing raw images that expose private account, contact, location, or support-case information.

---

## Interpretation boundary

This repository distinguishes between:

* raw observation
* derived technical interpretation
* hypothesis
* attribution

Raw artifacts are preserved to allow reviewers to test whether the interpretations are valid.

The public summaries should not be treated as final proof without private artifact review.

---

## No public raw dump

This repository is not intended to be a complete public dump of all artifacts.

It is intended to be a structured, privacy-preserving review package.

The goal is to make the technical question readable without exposing sensitive personal or device data.
