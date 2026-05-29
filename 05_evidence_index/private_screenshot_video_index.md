# Private Screenshot and Video Evidence Index

## Purpose

This file indexes private screenshot and video evidence referenced by this repository.

Raw screenshots and videos are not included in the public repository.

They are preserved privately because they may contain:

* Apple ID information
* personal account information
* Apple Support information
* location data
* contact data
* phone numbers
* device identifiers
* private UI state
* nearby address or network information

---

## Time zone

All summarized times use:

`UTC+7`

---

## Public rule

Do not publish raw screenshots or raw videos in this repository unless they are fully reviewed, redacted, and approved for public release.

This file should only contain:

* date
* approximate time
* evidence category
* public description
* private preservation status
* review purpose

---

## 2026-03-04 private evidence

### 2026-03-04 04:20 UTC+7

Evidence category:

`Apple Pay stopped notification`

Private status:

`preserved privately`

Public role:

This screenshot is a timestamp anchor for the 2026-03-04 Lost Mode / Apple Pay / device trust-state window.

Review purpose:

* verify notification timestamp
* verify Apple Pay stopped state
* compare with Lost Mode notification
* compare with Find My / AppleAccount / device-state artifacts

---

### 2026-03-04 04:21 UTC+7

Evidence category:

`Lost Mode enabled notification`

Private status:

`preserved privately`

Public role:

This screenshot is a primary timestamp anchor for the 2026-03-04 Lost Mode event.

Review purpose:

* verify Lost Mode activation timestamp
* compare with Find My / AppleAccount / location / sharing artifacts
* compare with Apple Pay stopped notification
* compare with nearby stackshot process context

---

### 2026-03-04 04:20-04:50 UTC+7

Evidence category:

`screenshot / video evidence window`

Private status:

`preserved privately`

Public role:

This window documents the user’s real-time device observation after the Apple Pay stopped and Lost Mode notifications.

Review purpose:

* verify user interaction window
* verify screenshot / video timestamps
* compare with Visual Intelligence / Photos / Spotlight / ANE activity
* compare with battery / thermal / disk-write context
* compare with Game Center UI exposure

---

### 2026-03-04 04:43 UTC+7

Evidence category:

`Game Center UI screenshot`

Private status:

`preserved privately`

Public role:

This screenshot reportedly shows Game Center UI involving friend discovery / friend suggestions / friend request context.

Review purpose:

* verify Game Center UI timestamp
* verify visible Game Center text
* compare with 2026-03-04 Game Center restriction baseline
* compare with 2026-03-05 Game Center restriction recomputation
* assess whether Game Center represents an exposed restriction-template seam

---

### 2026-03-04 23:13 UTC+7

Evidence category:

`ChatGPT physical-sensation report screenshot`

Private status:

`preserved privately`

Public role:

This screenshot reportedly shows a contemporaneous ChatGPT message describing an electricity-like sensation through the floor and tingling in the feet after returning home.

Boundary:

This is not treated as proof of an external physical source.

It is used only as timestamp context for active device interaction and observation.

Review purpose:

* verify message timestamp
* verify contemporaneous reporting
* compare with SFA / CloudServices / CKKS / PCS / SOS / Networking burst context
* compare with user-interaction / foreground app context

---

## 2026-03-05 private evidence

### 2026-03-05 05:11 UTC+7

Evidence category:

`Family Sharing screenshot`

Private status:

`preserved privately`

Public role:

This screenshot reportedly shows Family Sharing-related UI where the user appeared as organizer / manager.

Review purpose:

* verify screenshot timestamp
* verify visible Family Sharing state
* compare with Apple Support-side visibility context
* clarify what can be confirmed from UI evidence versus logs

Boundary:

Logs alone do not establish Family Sharing organizer status.

This screenshot is the relevant private UI evidence for that point.

---

### 2026-03-05 09:50 UTC+7

Evidence category:

`Contacts / phone-related screenshot`

Private status:

`preserved privately`

Public role:

This screenshot reportedly shows an unknown name / number context before the Apple Support contact window.

Review purpose:

* verify screenshot timestamp
* verify visible UI context
* preserve user-side timeline before Apple Support contact

Boundary:

This screenshot is contextual evidence only.

It is not treated as primary proof of device control or attribution.

---

### 2026-03-05 11:08 UTC+7

Evidence category:

`Find My screenshot`

Private status:

`preserved privately`

Public role:

This screenshot reportedly shows Find My location / device-state context shortly before Apple Support contact.

Review purpose:

* verify screenshot timestamp
* verify visible Find My context
* compare with Apple Support contact timing
* compare with location / device-state concerns

Boundary:

This screenshot is not treated as standalone proof of location manipulation.

It is used as pre-support user-side context.

---

### 2026-03-05 11:10-11:31 UTC+7

Evidence category:

`Apple Support interaction records`

Private status:

`preserved privately`

Public role:

These records are the main external timing anchor for 2026-03-05.

Review purpose:

* verify Apple Support interaction window
* verify case / interaction timeline
* verify support-side visibility / non-visibility findings
* compare with 11:11-11:14 ManagedSettings / DMD / Game Center recomputation window

Boundary:

Raw Apple Support records, case identifiers, account identifiers, and support screenshots are not public.

---

### 2026-03-05 18:11 UTC+7

Evidence category:

`Screen Time restriction-related screenshot`

Private status:

`preserved privately`

Public role:

This screenshot reportedly shows Screen Time restriction-related UI after the 11:11-11:14 internal recomputation window.

Review purpose:

* verify screenshot timestamp
* verify visible Screen Time restriction UI
* compare with Apple Support window
* compare with ManagedSettings / DMD restriction events
* compare with visible-management-absent artifact state

---

### 2026-03-05 18:12 UTC+7

Evidence category:

`Screen Time settings / Apple ID sign-out restriction video`

Private status:

`preserved privately`

Public role:

This video reportedly shows Screen Time settings and Apple ID sign-out restriction behavior.

Review purpose:

* verify video timestamp
* verify visible Screen Time settings
* verify Apple ID sign-out restriction behavior
* compare with MCState / ManagedSettings / DMD / Game Center artifacts
* compare with Apple Support-side visibility findings

This is one of the strongest private UI evidence anchors for 2026-03-05.

---

## Redaction requirements

Before any private screenshot or video is shared with a reviewer, consider redacting:

* Apple ID email address
* phone numbers
* contact names
* exact address strings
* precise location information
* BSSID / SSID values
* Apple Support case number
* payment / Apple Pay details
* device serial numbers
* account identifiers
* personal messages unrelated to the review

---

## Reviewer request requirements

If a qualified reviewer requests private screenshot or video evidence, the request should specify:

1. exact evidence item
2. date and approximate time
3. reason the public summary is insufficient
4. whether a redacted still image is enough
5. whether the full video is necessary
6. whether SHA256 verification is required
7. how the evidence will be stored and protected

---

## Boundary

This index does not prove:

* malware
* actor attribution
* Evil Twin / Rogue AP use
* malicious profile injection
* classic MDM enrollment
* Apple-side causation
* external physical source
* that Apple Support caused restriction events

It only indexes private screenshot and video evidence referenced by the public review package.
