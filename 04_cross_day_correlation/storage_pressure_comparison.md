# Storage Pressure Comparison

## Purpose

This file compares the storage-pressure and 1GB-class disk-write patterns across the three anchor dates:

* 2026-03-03
* 2026-03-04
* 2026-03-05

The purpose is to show why the disk-write pattern should be reviewed across dates rather than as isolated low-storage events.

---

## Summary

The reviewed artifacts showed repeated 1GB-class disk-write events across multiple processes and dates.

Public summary:

| Date       | Main process       | Public interpretation                                |
| ---------- | ------------------ | ---------------------------------------------------- |
| 2026-03-03 | fileproviderd      | FileProvider / SaveToFiles / storage-pressure anchor |
| 2026-03-04 | ANECompilerService | ANE / Visual Intelligence / Photos pressure          |
| 2026-03-04 | WeChat             | app / communication / storage pressure               |
| 2026-03-04 | fileproviderd      | FileProvider / Cloud / Photos / search pressure      |
| 2026-03-04 | sysdiagnosed       | diagnostic / speech / app / Photos pressure          |
| 2026-03-05 | WeChat             | app / communication / storage pressure               |

The key point is not that one disk-write event is abnormal.

The key point is that similar 1GB-class pressure appears repeatedly across several subsystems during the same three-day anchor sequence.

---

## 2026-03-03

Primary disk-write anchor:

* process: `fileproviderd`
* scale: 1GB-class write activity
* context: low free storage
* related public categories:

  * FileProvider
  * LocalStorageFileProvider
  * SaveToFiles
  * CloudDocs
  * cloudd
  * deleted
  * searchd
  * triald
  * parsecd
  * AppleAccount / accountsd context

Interpretation:

2026-03-03 is the FileProvider storage-pressure anchor.

It establishes the first major pressure event in the three-day sequence.

---

## 2026-03-04

2026-03-04 showed the strongest storage-pressure pattern.

Publicly summarized 1GB-class events included:

* `ANECompilerService`
* `WeChat`
* `fileproviderd`
* `sysdiagnosed`

This date is therefore treated as the main pressure / indexing / diagnostic concentration day.

---

## 2026-03-04 - ANECompilerService

Public summary:

* process: `ANECompilerService`
* scale: 1GB-class write activity
* related public categories:

  * ANE
  * Photos
  * Visual Intelligence
  * media analysis
  * model / compilation context

Interpretation:

This may be ordinary on-device model compilation or media-analysis pressure.

It remains relevant because it appears near the Lost Mode / Game Center / observation window.

---

## 2026-03-04 - WeChat

Public summary:

* process: `WeChat`
* scale: 1GB-class write activity
* related public categories:

  * messaging app context
  * storage pressure
  * communication context

Interpretation:

This should be compared with the 2026-03-05 WeChat pressure event.

The repeated WeChat pressure across adjacent dates may be ordinary cache/database behavior, but it is relevant to the cross-day pattern.

---

## 2026-03-04 - fileproviderd

Public summary:

* process: `fileproviderd`
* scale: 1GB-class write activity
* related public categories:

  * FileProvider
  * share-extension context
  * Cloud / Photos / search context
  * app-on-behalf-of context in private review

Interpretation:

This links the 2026-03-04 pressure pattern back to the 2026-03-03 fileproviderd anchor.

---

## 2026-03-04 - sysdiagnosed

Public summary:

* process: `sysdiagnosed`
* scale: 1GB-class write activity
* related public categories:

  * sysdiagnose / diagnostic generation
  * localspeechrecognition
  * Zalo
  * ChatGPT
  * WeChat
  * ANECompilerService
  * Photos
  * Gmail
  * SpringBoard

Interpretation:

This is important because diagnostic generation, speech recognition, AI/chat apps, messaging apps, Photos, and system pressure appear in the same broader context.

---

## 2026-03-05

Primary disk-write anchor:

* process: `WeChat`
* scale: 1GB-class write activity
* context: low free storage
* related public categories:

  * WeChat
  * communication app context
  * storage pressure
  * crash / log-writing context
  * later same-day Screen Time / Apple ID sign-out UI evidence context

Interpretation:

2026-03-05 is the WeChat storage-pressure anchor.

It appears on the same date as the Apple Support / ManagedSettings / DMD recomputation anchor.

---

## Cross-day pattern

The repeated pattern is:

1. 2026-03-03:

   * fileproviderd pressure

2. 2026-03-04:

   * ANE pressure
   * WeChat pressure
   * fileproviderd pressure
   * sysdiagnosed pressure

3. 2026-03-05:

   * WeChat pressure

Interpretation:

This suggests a repeated pressure chain across:

* FileProvider
* messaging apps
* Photos / Visual Intelligence / ANE
* diagnostics
* cloud/account/search/delete context

---

## Normal interpretation

Possible normal explanations include:

* low storage caused repeated disk-write resource reports
* WeChat cache or database activity caused large writes
* Photos / Visual Intelligence / ANE generated ordinary background writes
* FileProvider / SaveToFiles / share-extension behavior generated large writes
* sysdiagnose generation caused large diagnostic writes
* iOS log-writing limits and low free storage caused saved-zero or rejected logs

---

## Anomalous interpretation

The pattern remains important because:

* 1GB-class writes appeared repeatedly across three consecutive anchor dates
* multiple subsystems were involved, not only one app
* 2026-03-04 showed four separate 1GB-class write events
* pressure windows overlap with Lost Mode / Game Center / Apple Support / ManagedSettings contexts
* storage pressure may affect screenshot/video capture, log preservation, app stability, or evidence collection
* 2026-03-05 Analytics showed log-writing failure / saved-zero context in private review

---

## Review questions

Qualified reviewers should evaluate:

1. Are the repeated 1GB-class disk-write events normal under low-storage conditions?
2. Is the process distribution ordinary across FileProvider, WeChat, ANECompilerService, and sysdiagnosed?
3. Does the 2026-03-04 concentration indicate a normal background maintenance burst or an unusual pressure event?
4. Could storage pressure explain some later UI / log preservation issues?
5. Are FileProvider and iCloud Drive needs-auth states relevant to the disk-write pattern?
6. Are WeChat disk-write events on 2026-03-04 and 2026-03-05 ordinary app behavior?
7. Does sysdiagnosed pressure reflect normal diagnostic capture or a pressure artifact worth reviewing?

---

## Boundary

This file does not prove:

* malware
* actor attribution
* Evil Twin / Rogue AP use
* malicious profile injection
* classic MDM enrollment
* Apple-side causation
* intentional evidence suppression

This file only compares the repeated storage-pressure and disk-write pattern across the three anchor dates.
