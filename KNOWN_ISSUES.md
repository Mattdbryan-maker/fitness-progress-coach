# Known Issues

## Current Version: 0.8

No known critical issues remain following the Version 0.7 manual test cycle and the initial Version 0.8 Personal Records testing.

---

## Resolved Issues

- Fixed empty searches returning every workout.
- Fixed invalid numbered selections returning to the previous menu.
- Fixed invalid edit-menu selections exiting the feature.
- Fixed invalid weight values being saved to CSV.
- Fixed corrupted CSV data caused by invalid weight storage.
- Fixed date and weight update indentation.
- Fixed duplicated Workout Manager output.
- Fixed incorrect Edit Reps nesting.
- Fixed inconsistent variable names and spelling errors.
- Fixed menu retry and cancellation behaviour.
- Fixed inconsistent exercise capitalisation creating duplicate Personal Records.

---

## Future Improvements

- Add automated tests.
- Handle malformed CSV rows gracefully.
- Add a cancellation option to workout selection.
- Split the large `edit_workout()` function into smaller helper functions.
- Replace CSV storage with a database in a future version.
- Refactor Personal Record messages into reusable helper functions.
- Support multiple Personal Record types.
- Standardise exercise selection using an exercise library rather than free-text input.