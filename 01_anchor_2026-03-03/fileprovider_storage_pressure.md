# FileProvider and Storage Pressure - 2026-03-03

## Purpose

This file summarizes the FileProvider, iCloud Drive, storage-pressure, and memory-pressure observations for 2026-03-03.

This date is treated as the first artifact anchor.

---

## Summary

The 2026-03-03 artifacts showed a strong FileProvider / storage-pressure pattern.

Key observations:

* FileProvider activity present
* LocalStorageFileProvider / SaveToFiles context present
* iCloud Drive shown as logged out / not configured in `brctl`
* iCloud Drive FileProvider provider state still present as enabled / needs-auth
* large `fileproviderd` disk-write activity
* low free disk context
* memory pressure worsened through the evening
* Cloud / Account / Search / Delete / Trial process context appeared in nearby windows

The key point is not that FileProvider activity is automatically malicious.

The key point is that FileProvider / iCloud Drive / storage-pressure behavior appeared while visible management indicators were absent and while internal restriction-related structures were present.

---

## FileProvider state

Reviewed artifacts showed FileProvider-related state.

Relevant context included:

* `fileproviderd`
* `LocalStorageFileProvider`
* `SaveToFiles`
* `CloudDocs`
* iCloud Drive FileProvider provider state
* FileProvider indexing / scheduler context

Observed iCloud Drive state:

* `brctl` reported iCloud Drive logged out / not configured
* FileProvider still retained an iCloud Drive provider state
* iCloud Drive provider state appeared enabled / needs-auth

Interpretation:

This may be ordinary FileProvider behavior.

However, it should be reviewed because `brctl` and FileProvider showed different layers of iCloud Drive/account state.

---

## Main disk-write event

The primary storage-pressure event for 2026-03-03 was a large `fileproviderd` disk-write resource event.

Public summary:

* process: `fileproviderd`
* type: disk-write resource event
* approximate scale: 1GB-class write activity
* context: low free disk
* related areas: FileProvider / SaveToFiles / app-on-behalf-of context

Interpretation:

This event is important because similar 1GB-class write pressure appears again on 2026-03-04 and 2026-03-05.

---

## Evening pressure progression

The evening stackshot / sysdiagnose sequence showed increasing pressure.

Relevant windows:

* around 20:05 VN
* around 20:08 VN
* around 20:51 VN
* around 21:34 VN

Observed context included:

* FileProvider / LocalStorageFileProvider
* CloudDocs / cloudd / bird
* deleted / deleted_helper
* searchd
* triald
* parsecd
* suggestd
* appleaccountd
* accountsd
* CommCenter
* corespeechd

Interpretation:

The evening window shows FileProvider / Cloud / Account / Search / Delete / Trial activity coexisting with pressure conditions.

---

## Memory-pressure endpoint

The strongest reviewed memory-pressure point for this date appeared around the final evening stackshot / sysdiagnose window.

Public summary:

* free memory pages dropped sharply
* purgeable memory became very low
* pagesWanted increased
* process count remained high
* FileProvider / Cloud / Account / Search / Delete / Trial processes remained visible in the broader context

Interpretation:

This supports 2026-03-03 as a storage / memory-pressure anchor.

---

## Normal interpretation

Possible normal explanations include:

* low storage causing FileProvider pressure
* ordinary SaveToFiles / LocalStorageFileProvider behavior
* iCloud Drive not configured while FileProvider still retains provider metadata
* normal background iOS FileProvider indexing
* ordinary CloudDocs / cloudd / searchd / triald activity
* memory pressure caused by normal app and daemon workload

---

## Anomalous interpretation

The event remains relevant because:

* the large FileProvider write occurred under low free disk conditions
* similar 1GB-class write events recur on later reviewed dates
* FileProvider / iCloud Drive needs-auth state appears while `brctl` reports iCloud Drive not configured
* Cloud / Account / Search / Delete / Trial process clustering appears near the pressure window
* visible MDM / supervision / profile indicators were absent in the reviewed artifacts
* ManagedSettings / MCState structures were present on the same date

---

## Cross-day relevance

This date should be compared with:

### 2026-03-04

* multiple 1GB-class disk-write events
* ANECompilerService
* WeChat
* fileproviderd
* sysdiagnosed
* Lost Mode / Find My / Game Center / Visual Intelligence context

### 2026-03-05

* large WeChat disk-write event
* Apple Support window
* ManagedSettings / DMD / Game Center recomputation
* later Screen Time / Apple ID sign-out restriction UI evidence

---

## Boundary

This file does not prove:

* malware
* Evil Twin / Rogue AP use
* malicious profile injection
* actor attribution
* Apple-side causation
* classic MDM enrollment

This file only documents the FileProvider / iCloud Drive / storage-pressure pattern for 2026-03-03.
