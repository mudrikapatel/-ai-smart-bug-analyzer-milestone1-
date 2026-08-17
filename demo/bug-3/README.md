# Bug 3 — API 500 Internal Server Error

## Bug Type

REST API / Server Error

## Bug Report

The customer profile API returns HTTP 500 when requesting a profile containing incomplete address information.

## Error

```text
HTTP 500 Internal Server Error

TypeError:
Cannot read properties of undefined

at ProfileService.getAddress(ProfileService.js:203)
at ProfileController.getProfile(ProfileController.js:76)
```

## Triage Result

| Field      | Result      |
| ---------- | ----------- |
| Severity   | High        |
| Priority   | P1          |
| Component  | Profile API |
| Confidence | 90%         |

## Log Analysis

* Exception: `TypeError`
* Failure Point: `ProfileService.js:203`
* Code Path: `ProfileController → ProfileService`
* Failure Category: Missing/undefined data handling

## Historical Retrieval

```text
Historical Defect: BUG-3156
Similarity: 88%
```

## Root Cause

The service assumes that address data is always available and does not handle undefined values.

## Duplicate Detection

```text
Match 1: BUG-3156
Similarity: 88%

Match 2: BUG-3012
Similarity: 82%
```

## Recommended Fix

Add validation for missing address information and return a safe default or appropriate API response instead of allowing an undefined object to cause a server error.

## Final Status

**Analysis Completed**
