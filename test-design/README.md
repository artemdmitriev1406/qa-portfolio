# Test Design

Training artifacts demonstrating systematic coverage rather than ad-hoc checking.

## Techniques used

- Equivalence partitioning
- Boundary value analysis
- Decision tables
- State transition testing
- Positive and negative data design

## Example 1 — Name field

Requirement model used in the exercise:

- required field;
- 2–14 characters;
- Cyrillic letters;
- a hyphen or internal space may be valid;
- leading/trailing spaces, digits, Latin letters, and unsupported special characters are invalid.

| Class | Representative data | Expected result |
|---|---|---|
| Valid minimum | `Ар` | Accepted |
| Valid typical | `Артем` | Accepted |
| Valid maximum | 14 Cyrillic characters | Accepted |
| Below minimum | `А` | Validation error |
| Empty | empty value | Required-field error |
| Above maximum | 15 characters | Validation error |
| Latin letters | `Artem` | Validation error |
| Digits | `Артем14` | Validation error |
| Leading space | ` Артем` | Validation error |
| Internal hyphen | `Анна-Мария` | Accepted when total length is valid |

Boundary set: **0, 1, 2, 3, 13, 14, 15 characters**.

## Example 2 — Date field

Coverage includes:

- minimum and maximum supported year;
- month boundaries `00/01/02` and `11/12/13`;
- day boundaries for 28-, 29-, 30-, and 31-day months;
- leap-year behaviour;
- empty and incomplete values;
- invalid separators and characters;
- automatic input-mask formatting.

## Example 3 — Booking decision table

Three conditions determine the call to action:

- driving licence added;
- payment method added;
- route addresses completed.

| Licence | Payment | Addresses | Expected primary action |
|---|---|---|---|
| Yes | Yes | Yes | Book the car and show route duration/distance |
| No | Yes | Yes | Request licence details before booking |
| Yes | No | Yes | Request payment method before booking |
| No | No | Yes | Request licence first |
| Yes | Yes | No | Booking action remains available; route summary is hidden |
| No | Yes | No | Request licence details |
| Yes | No | No | Request payment method |
| No | No | No | Request licence first |

## What this demonstrates

- translating prose requirements into testable rules;
- eliminating redundant checks while preserving boundaries;
- identifying precedence between dependent conditions;
- separating representative values from boundary values;
- making expected behaviour explicit before execution.

The original spreadsheet contained additional classes and values; this public version is intentionally condensed and anonymized.