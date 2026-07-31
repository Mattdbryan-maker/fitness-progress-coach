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

## Day 3

### Version 0.5

#### Chronological Workout History

Successfully implemented chronological workout sorting using Python's `datetime` module.

### New Concepts Learned

- Importing Python modules
- `datetime.strptime()`
- Date formatting using `%d/%m/%Y`
- The `sorted()` function
- The `key=` parameter
- Lambda functions
- Sorting dictionary keys rather than dictionary values

This feature allows workouts to be displayed in true chronological order rather than the order they were added.

---

### Version 0.6

#### Workout Search System

Designed and implemented a dedicated workout search system.

Created a search submenu allowing users to choose between multiple search methods.

Features implemented:

- Search by Exercise
- Search by Date
- Partial exercise matching
- Case-insensitive exercise searching
- Multiple workout results
- No-match handling
- Return to main menu after searching

Searching by date also supports multiple workouts completed on the same day.

---

### Refactoring Progress

Improved the overall project structure by decomposing the search functionality into multiple smaller functions.

Instead of one large search function, the application now uses:

- `search_workouts()`
- `search_exercise()`
- `search_date()`

This makes the code easier to understand, maintain and extend.

---

### Testing

Successfully tested:

- Exact exercise search
- Partial exercise search
- Case-insensitive searching
- Search by date
- Multiple results returned
- Invalid exercise search
- Invalid date search

All tests passed successfully.

---

### Lessons Learned

Today was a significant step forward in learning software engineering rather than just Python syntax.

Key lessons included:

- Breaking large problems into smaller functions.
- Designing application architecture before writing code.
- Reusing existing code where possible.
- Understanding when code duplication should be refactored.
- Building software one feature at a time while maintaining clean structure.

---

### Current Version

Version 0.6

Current Features:

- Load workouts
- Save workouts
- View workouts
- Add workouts
- Chronological workout history
- Search workouts
    - Search by exercise
    - Search by date
- Dynamic sets and reps
- Input validation
- Git & GitHub

---

### Next Steps

Version 0.6 Refactor

- Create `display_workout(workout)` function.
- Remove duplicated display code.
- Improve maintainability.

Following that:

Version 0.7

- Edit workouts
- Delete workouts