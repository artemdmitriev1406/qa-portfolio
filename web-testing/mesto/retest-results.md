# Retest Results — Mesto

A later build was checked against previously reported defects.

| Area | Retest outcome | Comment |
|---|---|---|
| Application availability | Fixed | Main page opened successfully |
| Profile text overlap | Fixed | Layout matched the expected structure |
| One-character profile name | Fixed | Invalid value was no longer accepted |
| Image preview size | Fixed | Preview opened at the expected size |
| Like action and counter | Reopened | The icon and counter still did not update |
| Saving edited profile data | Reopened | New values still were not persisted |
| Image caption in preview | Fixed | Caption was displayed |
| Add-card action | Reopened | The add control was unavailable in the tested build |
| Card deletion | Reopened | Delete controls were absent |
| Closing profile modal | Fixed | Close control worked |
| Duplicate image after upload | Blocked by related defect | Could not verify because the add-card control was absent |
| Save-button activation | Fixed | Button state changed for valid data |
| Gallery scrolling | Fixed | Remaining cards became accessible |
| Closing card preview | Fixed | Preview closed correctly |
| Opening card image | Fixed | Image preview opened |

## Retest principles demonstrated

- A defect is closed only when the original scenario no longer reproduces.
- A related regression does not automatically mean the original defect is fixed.
- When a prerequisite is unavailable, the test is marked blocked rather than passed.
- Reopened defects include the current reproduction scenario and evidence from the new build.