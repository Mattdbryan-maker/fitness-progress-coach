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
  - Reps → `int`

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

"Today i really feel like i've kicked on from that first exciting day, i am really enjoying watching the foundations of this application really come together. I think i have made a lot of meaningful progress and am really hopeful for the future"

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