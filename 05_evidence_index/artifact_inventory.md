# Artifact Inventory

## Purpose

This file provides a public inventory of referenced artifacts for the three-anchor review package.

Raw artifacts are not included in this public repository.

This inventory lists artifact names and their review purpose.

---

## Time zone

All summarized times use:

`UTC+7`

---

## 2026-03-03 artifact inventory

Anchor role:

`FileProvider / MCState / ManagedSettings / visible-management-absent artifact anchor`

### Local log package

`Logs.zip`

Public status:

`not included`

Private status:

`preserved separately`

Review purpose:

* local logs
* stackshots
* Analytics
* RTCReporting
* SiriSearchFeedback
* CPU resource records
* FileProvider disk-write records
* memory / storage-pressure context

---

### Sysdiagnose archives

`sysdiagnose_2026.03.03_11-53-34+0700_iPhone-OS_iPhone_22F76.tar.gz`

Review purpose:

* MCState baseline
* ManagedSettings baseline
* visible management absence check
* ScreenTime / SafariStore baseline
* brctl / iCloud Drive state

---

`sysdiagnose_2026.03.03_12-14-27+0700_iPhone-OS_iPhone_22F76.tar.gz`

Review purpose:

* second MCState / ManagedSettings comparison point
* visible-management-absent state persistence
* mid-day baseline comparison

---

`sysdiagnose_2026.03.03_20-09-49+0700_iPhone-OS_iPhone_22F76.tar.gz`

Review purpose:

* FileProvider / SaveToFiles context
* LocalStorageFileProvider context
* iCloud Drive FileProvider provider state
* Wi-Fi / networking state
* evening pressure context

---

`sysdiagnose_2026.03.03_20-51-10+0700_iPhone-OS_iPhone_22F76.tar.gz`

Review purpose:

* evening MCState comparison
* visible management absence check
* ManagedSettings comparison
* FileProvider / iCloud Drive needs-auth context
* Wi-Fi / WWAN state

---

`sysdiagnose_2026.03.03_21-34-04+0700_iPhone-OS_iPhone_22F76.tar.gz`

Review purpose:

* final evening anchor
* MCState / ManagedSettings persistence check
* FileProvider / indexing context
* brctl / iCloud Drive state
* Wi-Fi / WWAN state
* memory-pressure endpoint

---

## 2026-03-04 artifact inventory

Anchor role:

`Lost Mode / Find My / Game Center exposure / ANE-VisualIntelligence pressure / Account-Cloud-Trust burst anchor`

### Local log package

`15G-2026-03-04.zip`

Public status:

`not included`

Private status:

`preserved separately`

Review purpose:

* local logs
* stackshots
* Analytics
* SFA records
* SiriSearchFeedback
* disk-write resource records
* CPU resource logs
* Wi-Fi quality logs
* sysdiagnose archive
* pressure / account / trust-state context

---

### Sysdiagnose archive

`sysdiagnose_2026.03.04_05-13-59+0700_iPhone-OS_iPhone_22F76.tar.gz`

Review purpose:

* MCState baseline after the 04:20-04:50 window
* visible management absence check
* ManagedSettings / ScreenTime baseline
* Game Center social restriction baseline
* Safari restriction baseline before 2026-03-05
* Wi-Fi / WWAN context
* brctl / iCloud Drive context
* Powerlog / BGSQL context

---

### Private UI evidence categories

Raw media is not public.

Private evidence reportedly includes:

* `2026-03-04 04:20 UTC+7` - Apple Pay stopped notification
* `2026-03-04 04:21 UTC+7` - Lost Mode enabled notification
* `2026-03-04 04:20-04:50 UTC+7` - screenshot/video evidence from main event window
* `2026-03-04 04:43 UTC+7` - Game Center UI screenshot
* `2026-03-04 23:13 UTC+7` - contemporaneous ChatGPT message screenshot reporting physical sensation

---

## 2026-03-05 artifact inventory

Anchor role:

`Apple Support interaction / ManagedSettings-DMD-Game Center recomputation / later Screen Time UI evidence anchor`

### Local log package

`15G-2026-03-05.zip`

Public status:

`not included`

Private status:

`preserved separately`

Review purpose:

* local logs
* stackshots
* Analytics
* RTCReporting
* crash records
* SiriSearchFeedback
* WeChat disk-write records
* xp_amp_app_usage_dnu records
* account / trust / storage-pressure context

---

### Sysdiagnose archives

`sysdiagnose_2026.03.05_04-02-35+0700_iPhone-OS_iPhone_22F76.tar.gz`

Review purpose:

* early-morning precondition context
* MCState / ManagedSettings baseline where available
* Wi-Fi / route context
* ScreenTime / Safari baseline before the 11:11-11:14 restriction window

---

`sysdiagnose_2026.03.05_04-14-45+0700_iPhone-OS_iPhone_22F76.tar.gz`

Review purpose:

* early-morning network / route transition context
* ManagedSettings / ScreenTime baseline where available
* precondition window comparison

---

`sysdiagnose_2026.03.05_05-13-59+0700_iPhone-OS_iPhone_22F76.tar.gz`

Review purpose:

* early-morning precondition context
* brctl / iCloud Drive context
* route / networking context
* ScreenTimeEnabled_CurrentUser baseline

---

`sysdiagnose_2026.03.05_08-20-59+0700_iPhone-OS_iPhone_22F76.tar.gz`

Review purpose:

* partial pre-support state context
* baseline comparison before the 11:10-11:31 support window

---

`sysdiagnose_2026.03.05_18-11-13+0700_iPhone-OS_iPhone_22F76.tar.gz`

Review purpose:

* post-support ManagedSettings / MCState comparison
* visible-management absence check
* FileProvider / Wi-Fi / brctl context
* near the later Screen Time UI evidence window

---

`sysdiagnose_2026.03.05_21-22-25+0700_iPhone-OS_iPhone_22F76.tar.gz`

Review purpose:

* later post-support state comparison
* ManagedSettings / SafariStore state
* Game Center / EffectiveUserSettings comparison
* FileProvider / iCloud Drive needs-auth context
* WeChat disk-write / storage-pressure comparison context

---

### Private UI / support evidence categories

Raw media and support records are not public.

Private evidence reportedly includes:

* `2026-03-05 05:11 UTC+7` - Family Sharing screenshot
* `2026-03-05 09:50 UTC+7` - Contacts / phone-related screenshot
* `2026-03-05 11:08 UTC+7` - Find My screenshot
* `2026-03-05 11:10-11:31 UTC+7` - Apple Support interaction records
* `2026-03-05 18:11 UTC+7` - Screen Time restriction-related screenshot
* `2026-03-05 18:12 UTC+7` - Screen Time settings / Apple ID sign-out restriction video

---

## Cross-date key artifact categories

### MCState / ManagedSettings

Review purpose:

* visible management absence
* EffectiveUserSettings comparison
* Safari restriction state
* Game Center social restriction state
* DMD / Digital Health recomputation

---

### FileProvider / iCloud Drive

Review purpose:

* FileProvider provider state
* iCloud Drive needs-auth context
* brctl not-configured state
* LocalStorageFileProvider / SaveToFiles context

---

### Storage-pressure records

Review purpose:

* fileproviderd 1GB-class write
* ANECompilerService 1GB-class write
* WeChat 1GB-class write
* sysdiagnosed 1GB-class write
* low-storage / log-writing failure context

---

### Account / Cloud / Trust records

Review purpose:

* AppleAccount
* accountsd
* CKKS
* PCS
* SOS
* CloudServices
* networking health
* RTCReporting / SFA records

---

### User-side UI evidence

Review purpose:

* Lost Mode / Apple Pay stopped timestamp
* Game Center UI timestamp
* Apple Support window
* Family Sharing context
* Find My context
* Screen Time / Apple ID sign-out restriction UI

---

## Boundary

This inventory does not prove:

* malware
* actor attribution
* Evil Twin / Rogue AP use
* malicious profile injection
* classic MDM enrollment
* Apple-side causation

It only lists the artifacts referenced by the public review package.
