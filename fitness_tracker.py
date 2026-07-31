import csv
from datetime import datetime
import ast

seperator = "=" * 50

def load_workouts(filename):
    workouts = []

    with open (filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            row["Weight"] = float(row["Weight"])
            row["Sets"] = int(row["Sets"])
            row["Reps"] = ast.literal_eval(row["Reps"])
            workouts.append (row)
    return (workouts)

workouts = load_workouts("workouts.csv")

def save_workouts(filename, workouts):

    field_names = ["Date", "Exercise", "Weight", "Sets", "Reps"]

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)

        writer.writeheader()

        for workout in workouts:
            writer. writerow(workout)

def view_workouts(workouts):

    if not workouts:
        print("No Workouts Found")
        return

    workouts_by_date = {}

    for workout in workouts:
        date = workout["Date"]
        workouts_by_date.setdefault(date, []).append(workout)     

    sorted_dates = sorted((workouts_by_date),
                           key=lambda date: datetime.strptime(date, "%d/%m/%Y")
                           ) 
    for date in sorted_dates:
        daily_workouts = workouts_by_date[date]

        print(seperator)
        print(f'Workout on {date}')
        print(seperator)

        for workout in daily_workouts:
            print (f'Exercise: {workout["Exercise"]}')
            print (f'Weight: {workout["Weight"]} kg')
            print (f'Total Sets: {workout["Sets"]}')
            print ()

            for set_number, reps in enumerate(workout["Reps"], start = 1):
                print (f'Set {set_number}: {reps} reps ' 
                       f' @ {workout["Weight"] }kg'
                       )
            print ()
        
def add_workout(workouts):

    date = input('What was the date of this workout?:\n')
    exercise = input('What exercise did you complete?: \n')
    while True:
        try:
            weight = float(input('What weight did you use (kg)?: \n'))
            if weight >= 0:
                break
            else:
                print("Please enter a numebr greater than or equal to 0")
        except ValueError:
            print()
            print("Please enter a valid number.")
           
    while True:   
        try:     
            total_sets = int(input('How many sets did you complete?: \n'))
            if total_sets > 0:
                reps = []
                for current_set in range(1, total_sets + 1):

                    while True:
                        try:
                            reps_completed = int(input(f'How many reps did you complete in set {current_set}?: \n'))
                            if reps_completed > 0:
                                reps.append(reps_completed)
                                break
                            else:
                                print()
                                print('Please input a number greater than 0.')
                        except ValueError:
                            print()
                            print('Please enter a valid whole number.')
                        
                break
            else:
                print('Please input a number greater than 0')
                print()
        except ValueError:
            print()
            print("Please enter a valid whole number.")
            

    new_exercise = {"Date": date,
                    "Exercise": exercise,
                    "Weight": weight,
                    "Sets": total_sets,
                    "Reps": reps
                    }
    workouts.append(new_exercise)
    return workouts

def show_menu():
      print(seperator)
      print("Fitness Progress Coach".center(50))
      print(seperator)
      print ()
      print('1. View Workouts')
      print('2. Add Workout')
      print('3. Serach Workouts')
      print('4. Exit')
      print()

def search_date(workouts):
        
    serach_date = input("Enter the date, to view the corresponding workout: "
                               ).strip()
    matches = []
    for workout in workouts:
        if serach_date in workout["Date"]:
            matches.append(workout)
    if not matches:
            print()
            print ("No matching Date found")
            print()
    else:
        for match in matches:
            print ()
            print(seperator)
            print(f'Workout on {match["Date"]}')
            print(seperator)
            print (f'Exercise: {match["Exercise"]}')
            print (f'Weight: {match["Weight"]} kg')
            print (f'Total Sets: {match["Sets"]}')
            print ()
                
            for set_number, reps in enumerate(match["Reps"], start = 1):
                print (f'Set {set_number}: {reps} reps '
                        f' @ {match["Weight"] }kg'
                     )

def search_exercise(workouts):
    
    serach_exercise = input("Enter the name of a Exercise, to view previous stats: "
                               ).strip().lower()
    matches = []
    for workout in workouts:
        if serach_exercise in workout["Exercise"].lower():
            matches.append(workout)
    if not matches:
            print()
            print ("No matching Exercises found")
            print()
    else:
        for match in matches:
            print ()
            print(seperator)
            print(f'Workout on {match["Date"]}')
            print(seperator)
            print (f'Exercise: {match["Exercise"]}')
            print (f'Weight: {match["Weight"]} kg')
            print (f'Total Sets: {match["Sets"]}')
            print ()
                
            for set_number, reps in enumerate(match["Reps"], start = 1):
                print (f'Set {set_number}: {reps} reps '
                        f' @ {match["Weight"] }kg'
                     )

def search_workouts(workouts):

    print()
    print(seperator)
    print("Search Workouts")
    print(seperator)
    print()
    print("1. Search by Exercise")
    print("2. Serach by Date")
    print("3. Return")

    choice = int(input("Choose an option:"))

    if choice == 1:
        search_exercise(workouts)

    elif choice == 2:
        search_date(workouts)

    elif choice == 3:
        return

    else:
        print ("Invalid option")
                
def main():
    file_path = "workouts.csv"
    workouts = load_workouts(file_path)
    running = True
    
    while running:

        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_workouts(workouts)

        elif choice == "2":

            adding_exercise = True

            while adding_exercise:
                add_workout(workouts)

                while True:
                    print()
                    another_workout = input(
                        "Would you like to add another Workout. Please enter y or n: "
                    ).lower()

                    if another_workout == "n":
                        adding_exercise = False
                        break

                    elif another_workout == "y":
                        break
                    
                    else:   
                        print("Inavlid input. Please enter y or no")

            save_workouts(file_path, workouts)
            print ("Workout added and saved successfully.")

        elif choice == "3":
            search_workouts(workouts)

        elif choice == "4":
            running = False
            print()
            print("Program closed")

        else:
            print ("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()

 