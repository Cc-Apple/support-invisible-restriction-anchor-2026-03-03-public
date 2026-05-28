# Non-Attribution Statement

This repository does not claim that any specific actor, APT group, state, company, government, organization, or individual is responsible for the observed artifacts.

This repository documents a technical artifact correlation from 2026-03-03 for qualified forensic review.

## What is claimed

The current claim is limited to the following:

```text
The device reportedly displayed an Apple ID sign-out restriction on 2026-03-03.

Apple Support was reportedly contacted on the same date.

Apple Support reportedly could not confirm a visible Screen Time, Family Sharing, MDM, or supervised-management restriction from their side.

The same date contains preserved artifact references showing ManagedSettings / ScreenTime / MCState / Analytics-related structure.
```

The referenced artifact structure includes:

```text
ManagedSettings / ScreenTime local stores
MCState showing IsSupervised:false
MCState showing PostSetupProfileWasInstalled:false
visible profile / payload structures appearing empty
next-day Analytics showing MDMStatus:false
same-day crash / CPU resource / FileProvider side effects
```

## What is not claimed

This repository does not establish:

```text
malware
payload
C2
exploit chain
APT attribution
state attribution
Apple attribution
criminal attribution
identity of an attacker
MDM enrollment
```

## Purpose

The purpose of this repository is to support a qualified DFIR / mobile forensic review of whether the observed artifact correlation is technically meaningful.

This repository is not intended to assign blame.

It is not intended to identify an attacker.

It is not intended to prove compromise by itself.

## Review boundary

The key review question is not:

```text
Who did this?
```

The key review question is:

```text
Can the reported device-side Apple ID sign-out restriction and the observed ManagedSettings / ScreenTime / MCState / Analytics artifacts be explained by normal iOS behavior, or does the structure justify deeper mobile forensic review?
```

## Evidence boundary

Raw iOS logs and raw sysdiagnose archives are not included in this public repository.

The original raw evidence is preserved separately and can be provided later through a secure upload method, NDA, or evidence-handling procedure if required by a qualified reviewer.
