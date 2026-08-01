# Daily Progress

---

# Day 1

## Objective

Begin development of the Fitness Progress Coach application and establish the project's foundation.

---

## Completed

### Project Setup

- Created the `fitness_progress_coach` project.
- Created the following project files:
  - `fitness_tracker.py`
  - `workouts.csv`
  - `README.md`
  - `PROJECT_PLAN.md`
  - `DAILY_PROGRESS.md`
  - `KNOWN_ISSUES.md`
  - `FUTURE_IDEAS.md`

---

### Core Development

#### Data Loading

- Implemented `load_workouts()`.
- Successfully loaded workout data using `csv.DictReader`.
- Stored workout records as a list of dictionaries.
- Converted:
  - Weight → `float`
  - Sets → `int`
  - Reps → list of integers

#### Data Saving

- Implemented `save_workouts()`.
- Successfully wrote workout dictionaries back to the CSV file using `DictWriter`.

#### Workout History

- Implemented `view_workouts()`.
- Displayed every workout stored in the CSV.
- Added separators between workouts for readability.
- Successfully tested using placeholder workout data.

---

## Problems Solved

- Understood that all CSV values are initially loaded as strings.
- Learned when to convert values to `int` and `float`.
- Understood how to loop through a list of dictionaries.
- Learned that loop variables (such as `workout`) are created automatically during iteration.
- Fixed a `FileNotFoundError` caused by an incorrect file path.
- Understood the difference between reading dictionary values and modifying them.

---

## Lessons Learned

- Reading CSV files using `DictReader`.
- Writing CSV files using `DictWriter`.
- Lists of dictionaries.
- Data type conversion.
- Dictionary key access.
- Function responsibilities.
- Thinking about data structures before writing code.
- Planning software before building features.

---

## Project Planning

Created documentation to manage the project professionally:

- Project roadmap
- Daily development log
- Future ideas list
- Known issues tracker
- README

---

## Current Progress

### Completed Versions

- ✅ v0.1 – Load workouts from CSV
- ✅ v0.2 – Save workouts to CSV
- ⏳ v0.3 – Add workout (Next)
- ✅ v0.4 – View workout history

---

## Reflection

Today the project evolved from an idea into a functioning application.

Although the application is still simple, it can already:

- Read workout data.
- Store workout data.
- Display workout history.

More importantly, the project now has a clear roadmap, documentation, version tracking and a solid software foundation that can be expanded over time.

---

## Next Objective

Implement `add_workout()` and continue building towards the first usable version of the application.

"Today was one of the most exciting coding sessions I've had. For the first time, this feels less like learning Python and more like building a real product. I can genuinely see the long-term potential of this project, and I'm excited to see where it goes."

# Day 2

## Objective

Continue developing the Fitness Progress Coach by making the application interactive, improving the workout logging experience, and adding stronger input validation.

---

## Completed

### Add Workout Feature

- Implemented `add_workout()`.
- Added inputs for:
  - Date
  - Exercise
  - Weight
  - Total sets
  - Reps completed for each set
- Used a loop so the number of rep inputs automatically matches the number of sets.
- Stored reps as a list.
- Appended new workout dictionaries to the existing workouts list.
- Saved newly added workouts to the CSV file.

---

### Main Application Menu

- Created `main()`.
- Created `show_menu()` to keep `main()` clean.
- Added menu options for:
  - Viewing workouts
  - Adding workouts
  - Exiting the application
- Added a centred application title and separators for improved presentation.

---

### Improved Workout Display

- Updated `view_workouts()`.
- Displayed each individual set clearly.
- Added weight units.
- Displayed workouts in the following format:

  - Exercise
  - Weight
  - Total sets
  - Reps completed in each set

---

### Input Validation

Added validation for:

- Invalid weight inputs
- Negative weight values
- Invalid total set inputs
- Zero or negative sets
- Invalid rep inputs
- Zero or negative reps
- Invalid yes/no responses
- Invalid menu choices

Used:

- `try`
- `except ValueError`
- `while True`
- `if` statements
- nested validation loops

---

### Multiple Exercise Entry

- Allowed users to add multiple exercises without returning to the main menu.
- Added a yes/no prompt after each exercise.
- Added validation so only `y` or `n` is accepted.
- Saved the completed workout after all exercises were entered.

---

### Workout Grouping

- Grouped exercises completed on the same date.
- Created a dictionary where:
  - each key represents a date;
  - each value contains a list of workout dictionaries.
- Used `setdefault()` to build the grouped workout history.
- Displayed each date once with all corresponding exercises underneath it.

---

## Problems Solved

- Correctly handled mutable workout lists.
- Fixed workouts not saving to the CSV.
- Converted saved rep strings back into Python lists using `ast.literal_eval()`.
- Fixed nested-loop and `break` placement issues.
- Learned the difference between:
  - type validation using `try/except`;
  - logical validation using `if` statements.
- Improved the flow of adding multiple exercises.
- Restructured workout history by date.

---

## Lessons Learned

- Exception handling
- Input validation
- Nested loops
- Nested validation loops
- Dictionary grouping
- `setdefault()`
- `enumerate()`
- CSV list storage
- `ast.literal_eval()`
- Main application structure
- User experience design
- Refactoring functions
- Persistent data storage

---

## Current Features

- ✅ Load workouts
- ✅ Save workouts
- ✅ View workouts
- ✅ Add workouts
- ✅ Dynamic sets and reps
- ✅ Main menu
- ✅ Input validation
- ✅ Multiple exercise entry
- ✅ Group workouts by date

---

## Next Objective

Sort workout dates chronologically using Python's `datetime` module.

"Today I really feel like I've kicked on from that first exciting day, I am really enjoying watching the foundations of this application really come together. I think i have made a lot of meaningful progress and am really hopeful for the future"

# Day 3

## Objectives

- Implement chronological workout sorting.
- Complete Version 0.6 search functionality.
- Begin Version 0.7 workout management features.
- Continue improving code quality through refactoring.

---

## Features Implemented

### Chronological Workout Display

Implemented chronological sorting of workouts using Python's `datetime` module.

Learned and applied:

- `datetime.strptime()`
- `sorted()`
- `key=` parameter
- `lambda` functions

Workouts are now displayed from the earliest date to the most recent while still grouping exercises performed on the same day.

---

### Search Workouts

Completed Version 0.6.

Implemented:

- Search by exercise.
- Search by date.
- Partial exercise matching.
- Case-insensitive searching.
- Handling of searches with no matching workouts.

Created a dedicated Search Workouts submenu to improve navigation.

Version 0.6 is now complete.

---

### Refactoring

Refactored duplicated code to improve readability and maintainability.

Created:

- `display_workout(workout)` – responsible for displaying a single workout.
- `select_workout(workouts)` – responsible for searching, displaying and returning a selected workout.

This significantly reduced duplicated code throughout the project and applied the DRY (Don't Repeat Yourself) principle.

---

### Delete Workout

Implemented the complete workout deletion workflow.

Features include:

- Search for workouts by exercise.
- Display numbered matching workouts.
- Validate workout selection.
- Display the selected workout before deletion.
- Confirmation prompt before deleting.
- Ability to cancel deletion.
- Permanent removal from the CSV file.
- Success confirmation after deletion.

Fully tested and confirmed working.

---

### Edit Workout

Started implementation of the workout editing system.

Completed editing of:

- Exercise name
- Weight
- Date

Added validation for each field:

Exercise:
- Cannot be left blank.

Weight:
- Must be a valid number.
- Must be greater than or equal to zero.

Date:
- Must be entered in `dd/mm/yyyy` format.
- Validated using `datetime.strptime()` to ensure real calendar dates.

Editing of Sets and Reps remains the final feature before completing Version 0.7.

---

## Testing

Successfully tested:

- Chronological workout sorting.
- Search by exercise.
- Search by date.
- Partial matching.
- No-match handling.
- Workout deletion.
- Confirmation prompts.
- Invalid confirmation inputs.
- CSV persistence after deletion.
- Exercise editing.
- Weight editing.
- Date editing.
- Input validation for text, numbers and dates.

---

## Lessons Learned

Today's development focused heavily on improving software structure rather than simply adding features.

Key concepts learned:

- Creating reusable helper functions.
- Returning dictionaries from functions.
- Refactoring duplicated code.
- Updating dictionary values without recreating the dictionary.
- Data-type specific validation.
- Using exceptions (`try` / `except`) for user input validation.
- Using `datetime.strptime()` for date validation.

This was my biggest step so far towards thinking about software architecture rather than individual pieces of code.

---

## Current Project Status

### Version 0.6 ✅ Complete

- Search workouts
- Search by exercise
- Search by date

### Version 0.7 🚧 In Progress

Completed:
- Delete workouts
- Edit exercise
- Edit weight
- Edit date

Remaining:
- Edit sets and reps

---

## Next Session

Complete the remaining Edit Sets and Reps functionality before moving on to the next planned version.

Continue refactoring where appropriate to keep the code modular and reusable.

## Day 4 Starting Point

Complete the `Edit Sets and Reps` option inside `edit_workout()`.

Planned flow:

1. Ask for the new total number of sets.
2. Validate that it is a positive integer.
3. Create a fresh reps list.
4. Ask for reps for every set.
5. Validate each rep value.
6. Replace both `"Sets"` and `"Reps"` in the selected workout.
7. Save the updated CSV.
8. Display the updated workout.

# Day 4

## Main Objective

Complete, test and stabilise Version 0.7 of the Fitness Progress Coach before beginning development of Version 0.8.

---

## Version 0.7 Completed

Version 0.7 introduced full workout management functionality.

The application now supports complete CRUD operations:

- Create — Add workouts
- Read — View and search workouts
- Update — Edit workouts
- Delete — Remove workouts

---

## Edit Workout

Completed the full Edit Workout feature.

Users can now edit:

- Exercise name
- Weight
- Date
- Total number of sets
- Reps for individual sets

### Exercise Editing

- Allows the exercise name to be changed.
- Rejects empty input.
- Saves the new exercise name permanently to the CSV file.

### Weight Editing

- Accepts whole numbers and decimal values.
- Rejects text input.
- Rejects negative weights.
- Allows zero for bodyweight exercises.
- Saves the updated weight permanently.

### Date Editing

- Requires the `dd/mm/yyyy` format.
- Rejects invalid dates.
- Rejects impossible calendar dates such as `31/02/2026`.
- Uses `datetime.strptime()` for validation.
- Updated workouts remain correctly ordered chronologically.

### Sets and Reps Editing

Users can choose between:

1. Replacing the total number of sets and entering a new reps list.
2. Keeping the same number of sets and editing individual rep values.

The individual reps menu:

- Displays each current set.
- Allows multiple sets to be edited.
- Validates the selected set number.
- Validates the new rep value.
- Includes a dynamic Return option.
- Saves all changes when editing is complete.

---

## Refactoring

Created and reused the following helper functions:

### `display_workout(workout)`

Displays a single workout consistently throughout the application.

Used by:

- View Workouts
- Search Workouts
- Edit Workout
- Delete Workout

### `select_workout(workouts)`

Handles:

- Searching for an exercise.
- Displaying matching workouts.
- Numbering the results.
- Validating the selected workout.
- Returning the chosen workout dictionary.

Used by:

- Edit Workout
- Delete Workout

### `get_sets_and_reps()`

Handles:

- Total set validation.
- Rep input for each set.
- Positive whole-number validation.
- Returning the completed set count and reps list.

Used by:

- Add Workout
- Edit Sets and Reps

These refactors reduced duplicated code and applied the DRY principle.

---

## Bugs Identified and Fixed

Today's testing uncovered and resolved several important bugs:

- Empty exercise searches previously matched every workout.
- Invalid numbered selections returned users to the previous menu instead of allowing another attempt.
- Invalid Edit Workout menu choices exited the edit menu.
- Invalid weight input could be saved as an empty value.
- Corrupted CSV data prevented the application from loading.
- Date and weight saving logic had incorrect indentation.
- The Workout Manager menu was displayed twice.
- The individual reps menu had incorrect nesting.
- A misspelled variable caused an empty search to bypass validation.
- Several spelling and user-message inconsistencies were corrected.

---

## Testing Completed

Successfully tested:

- Adding workouts.
- Empty exercise validation.
- Invalid date validation.
- Invalid weight validation.
- Set and rep validation.
- Viewing workouts.
- Chronological workout sorting.
- Searching by exercise.
- Searching by date.
- Empty search handling.
- No-match handling.
- Editing exercise names.
- Editing weights.
- Editing dates.
- Replacing sets and reps.
- Editing individual sets.
- Editing multiple sets.
- Invalid menu selections.
- Invalid numbered workout selections.
- Cancelling edits.
- Deleting workouts.
- Cancelling deletions.
- CSV persistence after restarting the application.

All planned Version 0.7 manual tests passed.

---

## Current Project Status

### Version 0.7 — Complete and Stable

Current functionality:

- Add workouts
- View workout history
- Group workouts by date
- Chronological workout display
- Search by exercise
- Search by date
- Edit workouts
- Delete workouts
- Persistent CSV storage
- Input validation
- Nested menu navigation
- Reusable helper functions

---

## Lessons Learned

Today was the most technically challenging development session so far.

Key lessons included:

- Debugging nested loops and menu flows.
- Understanding how indentation affects program behaviour.
- Distinguishing between fixing code and repairing corrupted stored data.
- Preventing invalid data from reaching persistent storage.
- Tracing errors using Python tracebacks.
- Testing invalid input as thoroughly as valid input.
- Refactoring repeated logic into reusable helper functions.
- Persisting through difficult debugging rather than abandoning the feature.

The application is now a complete, tested CRUD console application.

---

## Beginning Version 0.8

Following the completion of Version 0.7, work began on the next major feature: the Personal Records system.

The objective of this feature is to move the application beyond simply recording workout data and begin recognising user progress automatically.

---

## Personal Records

Implemented the first version of the Personal Records system.

The application can now:

- Calculate the highest weight lifted for every exercise.
- Display Personal Records in a dedicated menu.
- Automatically detect when a newly logged workout is a new Personal Record.
- Distinguish between a first recorded exercise and a new Personal Record.
- Display congratulatory messages when a Personal Record is achieved.
- Calculate and display the improvement over the previous Personal Record.

---

## New Functions

### `calculate_weight_prs(workouts)`

Loops through every workout and calculates the highest recorded weight for each exercise.

Returns a dictionary containing the current Personal Records.

### `view_personal_records(workouts)`

Displays all Personal Records.

Features include:

- Alphabetical sorting.
- Clean formatted output.
- Dedicated menu option.

### `check_weight_pr(workouts, new_workout)`

Checks whether a newly entered workout exceeds the existing Personal Record.

Returns:

- Whether a new Personal Record has been achieved.
- The previous Personal Record for comparison.

---

## Application Improvements

Added a new main menu option:

- Personal Records

The application now automatically checks every newly logged workout against previous performances.

If a Personal Record is achieved, the application displays:

- Exercise name.
- Previous best.
- New best.
- Improvement.

If the exercise has never previously been recorded, the application instead recognises it as the user's first recorded performance.

---

## Additional Bugs Identified and Fixed

While implementing the Personal Records system an important data consistency issue was discovered.

Exercise names entered using different capitalisation, for example:

- Back Squat
- Back squat
- back squat

were incorrectly being treated as separate exercises.

This issue was resolved by standardising exercise names using `.title()` before storing them.

Benefits include:

- Accurate Personal Records.
- Consistent searching.
- Reliable future analytics.
- Improved data quality throughout the application.

---

## Additional Testing

Successfully tested:

- Personal Record calculation.
- Personal Record display.
- Main menu integration.
- New Personal Record detection.
- First recorded exercise detection.
- Improvement calculation.
- Exercise name standardisation.
- Existing exercise handling.
- Existing Personal Records remaining unchanged.
- Multiple Personal Records.

All Version 0.8 Personal Record tests passed successfully.

---

## Additional Lessons Learned

Today's second development session introduced several important software engineering concepts:

- Returning multiple values from functions.
- Separating calculation from presentation.
- Reusing existing functions instead of duplicating logic.
- Designing functions with a single responsibility.
- Standardising data at the point of entry.
- Thinking about user experience alongside functionality.
- Building reusable systems that can support future AI features.

The Personal Records feature now provides the foundation for future achievements, coaching suggestions and intelligent workout analysis.

---

## Next Session

Continue Version 0.8 by:

- Refactoring Personal Record messages into reusable helper functions.
- Implementing repetition Personal Records.
- Supporting multiple Personal Record categories.
- Beginning the Achievement System.
- Exploring intelligent coaching suggestions based on workout history.