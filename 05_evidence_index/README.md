# Evidence Index

## Purpose

This directory organizes the public evidence index for the three-anchor review package.

Raw artifacts are not included in this public repository.

This directory provides reviewer-facing references for:

* artifact inventory
* SHA256 reference index
* private screenshot / video evidence index
* raw artifact handling boundary

---

## Public evidence model

This repository uses a reference-based evidence model.

Public files may include:

* artifact names
* log titles
* sysdiagnose archive names
* approximate timestamps
* local device-observation time
* artifact category
* public interpretation
* normal interpretation
* anomalous interpretation
* private evidence ID
* SHA256 references where available

Public files must not include:

* raw logs
* raw sysdiagnose archives
* raw screenshots
* raw videos
* Apple ID identifiers
* phone numbers
* precise location data
* BSSID / SSID lists
* private contact data
* financial account data
* support-case identifiers unless redacted

---

## Evidence groups

The evidence package is organized around three dates.

### 2026-03-03

Role:

`FileProvider / MCState / ManagedSettings / visible-management-absent artifact anchor`

Primary private artifacts:

* local log ZIP
* sysdiagnose archives
* MCState / ManagedSettings records
* FileProvider records
* stackshots
* Analytics
* RTCReporting
* disk-write resource records

---

### 2026-03-04

Role:

`Lost Mode / Find My / Game Center exposure / ANE-VisualIntelligence pressure / Account-Cloud-Trust burst anchor`

Primary private artifacts:

* local log ZIP
* sysdiagnose archive
* Lost Mode / Apple Pay stopped screenshots
* Game Center UI screenshot
* physical-sensation report screenshot
* SFA / CloudServices / CKKS / PCS / SOS records
* disk-write resource records
* stackshots
* Wi-Fi / network records

---

### 2026-03-05

Role:

`Apple Support interaction / ManagedSettings-DMD-Game Center recomputation / later Screen Time UI evidence anchor`

Primary private artifacts:

* local log ZIP
* sysdiagnose archives
* Apple Support records
* Family Sharing screenshot
* Find My screenshot
* Screen Time restriction screenshot
* Screen Time / Apple ID sign-out restriction video
* MCState / ManagedSettings records
* RTCReporting
* WeChat disk-write records
* Analytics
* crash records

---

## Files in this directory

* `artifact_inventory.md`
  Public inventory of referenced artifacts by date.

* `sha256_reference_index.md`
  SHA256 reference index for preserved artifacts where available.

* `private_screenshot_video_index.md`
  Private screenshot and video evidence index without exposing raw media.

---

## Verification model

A qualified reviewer may request private artifacts to verify:

1. exact timestamps
2. exact log contents
3. exact MCState / ManagedSettings values
4. exact DMD / Digital Health / Game Center event paths
5. screenshot/video timestamps
6. Apple Support interaction records
7. SHA256 hashes
8. raw sysdiagnose contents

Raw artifacts should be shared only through a controlled review process.

---

## Boundary

This evidence index does not prove:

* malware
* actor attribution
* Evil Twin / Rogue AP use
* malicious profile injection
* classic MDM enrollment
* Apple-side causation

It only organizes the public references required for technical review.
