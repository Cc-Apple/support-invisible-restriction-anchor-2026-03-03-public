# Referenced Artifacts - 2026-03-05

## Purpose

This file lists the public artifact references for the 2026-03-05 anchor.

Raw artifacts are not included in this repository.

This file is an index for reviewers.

---

## Date

`2026-03-05`

Time zone used in summaries:

`UTC+7`

---

## Anchor role

2026-03-05 is treated as:

`Apple Support interaction / ManagedSettings-DMD-Game Center recomputation / later Screen Time UI evidence anchor`

This is the main Apple Support interaction date.

---

## Local log package

Referenced local log package:

`15G-2026-03-05.zip`

Public status:

`not included`

Private status:

`preserved separately`

Purpose:

Used to review 2026-03-05 local logs, stackshots, Analytics, RTCReporting, crash records, SiriSearchFeedback, WeChat disk-write records, xp_amp_app_usage_dnu records, and related system records.

---

## Main private screenshot / video evidence categories

Raw screenshots and videos are not included publicly.

Private evidence reportedly includes:

### 05:11 UTC+7

Family Sharing screenshot.

Public role:

* user-side Family Sharing / organizer-state context
* private UI evidence
* not derived from logs alone

---

### 09:50 UTC+7

Contacts / phone-related screenshot.

Public role:

* user-side pre-support context
* unknown name / number context
* private UI evidence only

---

### 11:08 UTC+7

Find My screenshot.

Public role:

* user-side pre-Apple Support context
* location / device-state concern context
* private UI evidence only

---

### 11:10-11:31 UTC+7

Apple Support interaction records.

Public role:

* primary external support-window anchor
* support-side visibility / non-visibility context
* private support evidence

---

### 18:11 UTC+7

Screen Time restriction-related screenshot.

Public role:

* later visible restriction UI evidence
* appears after the 11:11-11:14 restriction-state artifact window

---

### 18:12 UTC+7

Screen Time settings / Apple ID sign-out restriction video.

Public role:

* strongest later UI evidence anchor for the date
* used to compare visible UI state against MCState / ManagedSettings / Apple Support context

---

## Referenced sysdiagnose archives

The following sysdiagnose archives were reviewed.

Raw archives are not included publicly.

### 04:02 sysdiagnose

`sysdiagnose_2026.03.05_04-02-35+0700_iPhone-OS_iPhone_22F76.tar.gz`

Public role:

* early-morning precondition context
* MCState / ManagedSettings baseline where available
* Wi-Fi / route context
* ScreenTime / Safari baseline before the 11:11-11:14 restriction window

---

### 04:14 sysdiagnose

`sysdiagnose_2026.03.05_04-14-45+0700_iPhone-OS_iPhone_22F76.tar.gz`

Public role:

* early-morning network / route transition context
* ManagedSettings / ScreenTime baseline where available
* precondition window comparison

---

### 05:13 sysdiagnose

`sysdiagnose_2026.03.05_05-13-59+0700_iPhone-OS_iPhone_22F76.tar.gz`

Public role:

* early-morning precondition context
* brctl / iCloud Drive context
* route / networking context
* ScreenTimeEnabled_CurrentUser baseline

---

### 08:20 sysdiagnose

`sysdiagnose_2026.03.05_08-20-59+0700_iPhone-OS_iPhone_22F76.tar.gz`

Public role:

* partial pre-support state context
* baseline comparison before the 11:10-11:31 support window

Note:

This archive was limited / partial in private review.

---

### 18:11 sysdiagnose

`sysdiagnose_2026.03.05_18-11-13+0700_iPhone-OS_iPhone_22F76.tar.gz`

Public role:

* post-support ManagedSettings / MCState comparison
* visible-management absence check
* FileProvider / Wi-Fi / brctl context
* near the later Screen Time UI evidence window

---

### 21:22 sysdiagnose

`sysdiagnose_2026.03.05_21-22-25+0700_iPhone-OS_iPhone_22F76.tar.gz`

Public role:

* later post-support state comparison
* ManagedSettings / SafariStore state
* Game Center / EffectiveUserSettings comparison
* FileProvider / iCloud Drive needs-auth context
* WeChat disk-write / storage-pressure comparison context

---

## Important local log categories

The following 2026-03-05 local log categories were relevant in private review.

Raw files are not included publicly.

---

### MCState / ManagedSettings

Relevant for:

* Safari restriction change around 11:11 UTC+7
* DMD / Digital Health recomputation around 11:14 UTC+7
* Game Center social / friends-related restriction recomputation
* comparison against 2026-03-03 and 2026-03-04 baseline states

---

### Apple Support window

Relevant for:

* 11:10-11:31 UTC+7 support interaction
* support-side visibility / non-visibility context
* later comparison with device-side artifact changes

Raw Apple Support records are private.

---

### Screen Time UI evidence

Relevant for:

* 18:11 UTC+7 Screen Time restriction-related screenshot
* 18:12 UTC+7 Screen Time settings / Apple ID sign-out restriction video

Raw screenshot and video evidence are private.

---

### Game Center

Relevant for:

* Game Center restriction recomputation around 11:14 UTC+7
* comparison against 2026-03-04 Game Center UI exposure
* comparison against 2026-03-04 Game Center restriction baseline

---

### WeChat disk-write records

Relevant for:

* 1GB-class WeChat disk-write activity
* storage-pressure comparison against 2026-03-03 and 2026-03-04
* app / communication / storage-pressure context

---

### Stackshots

Relevant for:

* memory-pressure context
* FileProvider / CloudDocs / cloudd / deleted / searchd / triald / parsecd context
* AppleAccount / accountsd context
* CommCenter / corespeechd context
* app context around precondition and pressure windows

---

### Analytics

Relevant for:

* MDMStatus check
* LogWritingUsage context
* saved-zero / log-writing failure context
* app crash / storage-pressure context
* rejected / submitted log categories

---

### RTCReporting

Relevant for:

* AppleAccount / CKKS / Trust / MID-hash-related context
* account health records
* securityd / appleaccountd / accountsd / akd context

---

### xp_amp_app_usage_dnu

Relevant for:

* usageClientId changes
* app usage context
* WeChat / ChatGPT / DeepSeek / Gemini / Zalo / Google Drive / Chrome / Gmail / Alipay / MobilePhone / Notes / Find My / Signal / WhatsApp context

---

### Crash records

Relevant for:

* crash burst around the morning period
* CommCenter crash context
* MobilePhone / AlipayWallet / maild / ScreenshotServicesService context
* file-system-out-of-space context in reviewed private analysis

---

## Publicly summarized key findings

The public summaries derived from the referenced artifacts include:

* Apple Support interaction around 11:10-11:31 UTC+7
* ManagedSettings / Safari restriction changes around 11:11:38 UTC+7
* DMD / Digital Health recomputation shortly afterward
* Game Center social / friends-related restriction recomputation around 11:14 UTC+7
* later Screen Time / Apple ID sign-out restriction UI evidence around 18:11-18:12 UTC+7
* reviewed artifacts did not show ordinary visible MDM / supervision / profile indicators
* WeChat 1GB-class disk-write pressure occurred later the same day
* early-morning precondition activity appeared between 03:00 and 06:00 UTC+7

---

## Private verification required

A qualified reviewer may request private artifacts to verify:

* Apple Support interaction records
* support-side visibility / non-visibility statement
* Family Sharing screenshot timestamp
* Find My screenshot timestamp
* Screen Time restriction screenshot timestamp
* Screen Time / Apple ID sign-out restriction video timestamp
* MCState exact plist contents
* ManagedSettings exact plist contents
* DMD / Digital Health event paths
* Game Center restriction keys
* WeChat disk-write resource record
* RTCReporting account / trust records
* Analytics log-writing records
* stackshot process lists

Raw data is not included publicly due to privacy and security risk.

---

## Boundary

This artifact index does not prove:

* malware
* actor attribution
* Evil Twin / Rogue AP use
* malicious profile injection
* classic MDM enrollment
* Apple-side causation
* that Apple Support caused the restriction events
* that Game Center was the main target

It only lists the artifacts used to build the public 2026-03-05 summaries.
