# Referenced Artifacts - 2026-03-03

## Purpose

This file lists the public artifact references for the 2026-03-03 artifact anchor.

Raw artifacts are not included in this repository.

This file is an index for reviewers.

---

## Date

`2026-03-03`

Time zone used in summaries:

`VN time / UTC+7`

---

## Anchor role

2026-03-03 is treated as:

`FileProvider / MCState / ManagedSettings / visible-management-absent artifact anchor`

This date is not the Apple Support contact date.

---

## Local log package

Referenced local log package:

`Logs.zip`

Public status:

`not included`

Private status:

`preserved separately`

Purpose:

Used to review 2026-03-03 local logs, stackshots, Analytics, RTCReporting, FileProvider disk-write records, SiriSearchFeedback, CPU resource logs, and related system records.

---

## Referenced sysdiagnose archives

The following sysdiagnose archives were reviewed.

Raw archives are not included publicly.

### 11:53 sysdiagnose

`sysdiagnose_2026.03.03_11-53-34+0700_iPhone-OS_iPhone_22F76.tar.gz`

Public role:

* MCState baseline
* ManagedSettings baseline
* visible management absence check
* ScreenTime / SafariStore baseline
* brctl / iCloud Drive state

---

### 12:14 sysdiagnose

`sysdiagnose_2026.03.03_12-14-27+0700_iPhone-OS_iPhone_22F76.tar.gz`

Public role:

* second MCState / ManagedSettings comparison point
* confirms persistence of visible-management-absent state
* supports mid-day baseline comparison

---

### 20:09 sysdiagnose

`sysdiagnose_2026.03.03_20-09-49+0700_iPhone-OS_iPhone_22F76.tar.gz`

Public role:

* FileProvider / SaveToFiles context
* LocalStorageFileProvider context
* iCloud Drive FileProvider provider state
* Wi-Fi / networking state
* evening pressure context

Note:

This archive was lighter / partial compared with full sysdiagnose anchors.

---

### 20:51 sysdiagnose

`sysdiagnose_2026.03.03_20-51-10+0700_iPhone-OS_iPhone_22F76.tar.gz`

Public role:

* evening MCState comparison point
* visible management absence check
* ManagedSettings comparison
* FileProvider / iCloud Drive needs-auth context
* Wi-Fi / WWAN state context

Note:

Some archive-read issues were observed during private analysis, but relevant public-summary targets were readable.

---

### 21:34 sysdiagnose

`sysdiagnose_2026.03.03_21-34-04+0700_iPhone-OS_iPhone_22F76.tar.gz`

Public role:

* final evening anchor for the date
* MCState / ManagedSettings persistence check
* FileProvider / indexing context
* brctl / iCloud Drive state
* Wi-Fi / WWAN state
* memory-pressure endpoint

---

## Important local log categories

The following 2026-03-03 local log categories were relevant in private review.

Raw files are not included publicly.

### MCState / ManagedSettings

Relevant for:

* visible MDM absence
* supervision absence
* profile / payload absence
* EffectiveUserSettings baseline
* ScreenTime / SafariStore baseline

---

### FileProvider / disk writes

Relevant for:

* large `fileproviderd` disk-write activity
* FileProvider / SaveToFiles context
* LocalStorageFileProvider context
* iCloud Drive provider state
* low storage context

---

### Stackshots

Relevant for:

* memory-pressure progression
* FileProvider / CloudDocs / cloudd / deleted / searchd / triald / parsecd process context
* AppleAccount / Accounts process context
* CommCenter / corespeechd context

---

### Analytics

Relevant for:

* MDMStatus check
* log writing / log retirement context
* rejected / submitted telemetry categories
* storage/log handling context

---

### RTCReporting

Relevant for:

* AppleAccount / accountsd context
* account health / trust-state related records
* nearby support for account-cloud review

---

### SiriSearchFeedback

Relevant for:

* parsecd / spotlight / photos / visualintelligence-related feedback activity
* search / indexing context

---

### CPU resource logs

Relevant for:

* `ospredictiond`
* `signpost_reporter`
* system-resource context
* cloud/account/search/delete/trial process clustering

---

## Publicly summarized key findings

The public summaries derived from the referenced artifacts include:

* visible MDM / supervision / profile indicators were not observed
* MCState existed
* ManagedSettings existed
* ScreenTime / SafariStore baseline existed
* Safari private browsing / history clearing restrictions were not enabled on this date
* iCloud Drive was reported by `brctl` as logged out / not configured
* iCloud Drive FileProvider provider state appeared enabled / needs-auth
* LocalStorageFileProvider / SaveToFiles context was present
* a large `fileproviderd` disk-write event occurred
* memory pressure worsened in the evening
* Cloud / Account / Search / Delete / Trial process context appeared near key windows

---

## Private verification required

A qualified reviewer may request private artifacts to verify:

* MCState exact plist contents
* ManagedSettings exact plist contents
* FileProvider dump contents
* stackshot process lists
* Analytics metrics
* RTCReporting records
* disk-write resource records
* SHA256 values

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

It only lists the artifacts used to build the public 2026-03-03 summaries.
