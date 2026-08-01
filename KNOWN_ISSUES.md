# Known Issues

## Current Version: 0.7

No known critical issues remain following the Version 0.7 manual test cycle.

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

---

## Future Improvements

- Add automated tests.
- Handle malformed CSV rows gracefully.
- Add a cancellation option to workout selection.
- Split the large `edit_workout()` function into smaller helper functions.
- Replace CSV storage with a database in a future version.