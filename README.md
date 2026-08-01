# Fitness Progress Coach

A Python-based fitness tracking application for recording workouts, reviewing training history and monitoring long-term progress.

This project is being developed incrementally as the foundation for a future intelligent fitness-coaching platform.

---

## Current Version

**Version 0.7**

Version 0.7 is feature-complete and has passed the planned manual test suite.

---

## Current Features

### Workout Logging

- Add exercises to the workout history.
- Record workout dates.
- Record weight used.
- Record a dynamic number of sets.
- Record different reps for every set.
- Add multiple exercises during one session.

### Workout History

- Load workouts from CSV.
- Save workouts permanently.
- View all recorded workouts.
- Group exercises completed on the same date.
- Display workouts in chronological order.

### Search

- Search workouts by exercise.
- Search workouts by date.
- Partial exercise matching.
- Case-insensitive exercise matching.
- Display multiple matching results.
- Handle searches with no results.
- Reject empty searches.

### Workout Management

- Edit exercise names.
- Edit weight.
- Edit workout dates.
- Replace the total number of sets and reps.
- Edit reps for individual sets.
- Edit multiple sets before saving.
- Delete workouts.
- Confirm deletion before permanently removing data.
- Cancel editing or deletion safely.

### Validation

- Validate workout dates using `datetime.strptime()`.
- Reject impossible calendar dates.
- Reject empty exercise names.
- Reject invalid numerical input.
- Reject negative weights.
- Require positive whole numbers for sets and reps.
- Validate numbered menu selections.
- Validate `y/n` confirmation prompts.

---

## Technical Features

- Python
- CSV file storage
- Lists and dictionaries
- `csv.DictReader`
- `csv.DictWriter`
- `datetime`
- `ast.literal_eval`
- Functions and return values
- Nested loops
- Exception handling
- Input validation
- Chronological sorting
- Lambda functions
- Git version control
- GitHub project tracking

---

## Application Structure

```text
main()
│
├── show_menu()
├── add_workout()
│   └── get_sets_and_reps()
│
├── view_workouts()
│   └── display_workout()
│
├── search_workouts()
│   ├── search_exercise()
│   └── search_date()
│
└── manage_workouts()
    ├── edit_workout()
    │   ├── select_workout()
    │   ├── display_workout()
    │   └── get_sets_and_reps()
    │
    └── delete_workout()
        ├── select_workout()
        └── display_workout()
```

---

## Data Structure

Each workout is stored as a dictionary:

```python
{
    "Date": "01/08/2026",
    "Exercise": "Bench Press",
    "Weight": 85.0,
    "Sets": 4,
    "Reps": [10, 9, 8, 7]
}
```

Workout dictionaries are stored inside a list and persisted to `workouts.csv`.

---

## Development Roadmap

### Version 0.1

- ✅ Load workouts from CSV

### Version 0.2

- ✅ Save workouts to CSV

### Version 0.3

- ✅ Add workouts
- ✅ View workout history
- ✅ Dynamic sets and reps

### Version 0.4

- ✅ Interactive menu
- ✅ Multiple exercise entry
- ✅ Group exercises by date
- ✅ Input validation

### Version 0.5

- ✅ Chronological workout history
- ✅ Date handling with `datetime`

### Version 0.6

- ✅ Search workouts
- ✅ Search by exercise
- ✅ Search by date
- ✅ Partial and case-insensitive matching

### Version 0.7 — Current Version

- ✅ Edit workouts
- ✅ Delete workouts
- ✅ Edit individual sets and reps
- ✅ Reusable workout-selection logic
- ✅ Full CRUD functionality
- ✅ Comprehensive manual testing

### Version 0.8

- ⬜ Personal records
- ⬜ Progress tracking
- ⬜ Training volume

### Version 0.9

- ⬜ Workout sessions
- ⬜ Weekly summaries
- ⬜ Progress analysis

### Version 1.0

- ⬜ Complete and polished console application

---

## Development Progress

### Day 1

- Created the initial workout tracker structure.
- Loaded workout records from CSV.
- Displayed workout history.
- Began working with lists of dictionaries.

### Day 2

- Added workout logging.
- Added dynamic sets and reps.
- Added CSV saving.
- Added multiple exercise entry.
- Grouped workouts by date.
- Created the GitHub repository.

### Day 3

- Added chronological workout sorting.
- Built search by exercise and date.
- Created reusable display logic.
- Added workout deletion.
- Began workout editing.

### Day 4

- Completed full workout editing.
- Added individual set-rep editing.
- Refactored repeated set and rep logic.
- Improved validation throughout the application.
- Debugged menu-flow, indentation and persistent-data issues.
- Completed the Version 0.7 manual test suite.

---

## Long-Term Vision

The long-term goal is to develop the project into an intelligent fitness platform that can:

- Analyse workout history.
- Track strength and hypertrophy progress.
- Detect plateaus.
- Monitor training volume.
- Identify personal records.
- Provide personalised fitness guidance.
- Support goal and reward systems.
- Eventually provide AI-assisted coaching.
- Potentially include a progress-focused fitness community.

The immediate focus remains building and understanding a reliable backend before introducing a graphical interface or AI functionality.

---

## Running the Application

1. Ensure Python is installed.
2. Place `fitness_tracker.py` and `workouts.csv` in the same folder.
3. Run:

```bash
python fitness_tracker.py
```

---

## Project Status

Version 0.7 is currently:

- ✅ Feature complete
- ✅ Manually tested
- ✅ Persisting data successfully
- ✅ Ready for continued development

---
## About This Project

This project was not built as a tutorial or copied from an existing application.

It is being developed incrementally to strengthen my understanding of Python, software engineering principles and backend application development. Every version introduces new functionality while improving code quality through refactoring, testing and debugging.

The long-term goal is to evolve this application into an AI-assisted fitness platform.

## Author

Matthew Bryan

Built as part of my Python software development journey while learning programming and software engineering fundamentals.

GitHub: https://github.com/Mattdbryan