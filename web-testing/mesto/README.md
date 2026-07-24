# Mesto — Web Regression Testing

**Project type:** individual training project  
**Scope:** browser-based web application  
**Focus:** regression testing, profile-form validation, cards, modal windows, defect reporting, and retesting

## Objective

Assess whether the updated build preserves critical user flows and complies with the stated UI and validation requirements.

## Coverage

- application availability and initial page load;
- profile data display and editing;
- required fields and length validation;
- modal opening and closing;
- card gallery rendering and scrolling;
- image preview;
- likes and counters;
- adding and deleting cards;
- regression around corrected defects.

## Approach

1. Reviewed requirements and existing checks.
2. Prioritized blocking user journeys.
3. Executed positive, negative, and boundary scenarios.
4. Recorded defects with environment, steps, expected and actual results.
5. Retested a later build.
6. Classified defects as closed or reopened based on reproducibility.

## Selected artifacts

- [Selected bug reports](bug-reports.md)
- [Retest results](retest-results.md)

## Key findings

The tested builds contained failures affecting profile persistence, form validation, card management, modal behaviour, and like functionality. During retest, some defects were confirmed fixed, while others remained reproducible or became blocked by a related regression.

## Tools

- Yandex Browser / Chromium-based browser
- Browser DevTools
- Figma/reference layouts
- Spreadsheet-based test documentation

> The public version excludes the active training-environment URL and reproduces only selected artifacts.