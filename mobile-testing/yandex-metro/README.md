# Yandex Metro — Android Application Testing

**Project type:** individual training project  
**Platform:** Android emulator  
**Focus:** regression after application changes, device state, connectivity, UI settings, route history, and embedded web content

## Test environment

- Android 9 Pie emulator
- 1080 × 1920 resolution
- 5.5-inch virtual device
- Android Studio, Emulator, ADB, and Logcat

## Main coverage

- application launch and core navigation;
- route creation and station selection;
- preservation of selected data after orientation changes;
- route-history behaviour;
- automatic dark-theme switching around configured time boundaries;
- behaviour without network connectivity;
- error messages and recovery;
- feedback page opened through WebView;
- element positions and responsive behaviour;
- regression of changed screens.

## Representative scenarios

### Orientation change

1. Build a route.
2. Rotate the device.
3. Verify that selected stations, route result, and current screen state are preserved.

### Offline mode

1. Disable network connectivity.
2. Perform an action that requires remote data.
3. Verify that the application remains stable and shows a clear error message.
4. Restore connectivity and verify recovery.

### Automatic theme

Check transitions around both configured boundaries, including the minute before, exact boundary, and minute after.

### WebView feedback

Verify opening, navigation, back behaviour, network error handling, and return to the native application.

## Test design used

- boundary value analysis for time-based switching;
- pairwise testing for combinations of city, language, and theme;
- state-transition checks for route history and selected stations;
- regression checklist for changed functionality.

## What this demonstrates

- understanding of Android-specific risks;
- testing state preservation and lifecycle behaviour;
- use of emulator and logs for localization;
- coverage optimization with pairwise combinations;
- separation of native and WebView behaviour.

> This public summary excludes temporary builds, internal links, and full assignment text.