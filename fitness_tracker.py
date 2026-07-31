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
            display_workout(workout)
        
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
      print('4. Manage Workouts')
      print('5. Exit')
      print()

def display_workout(match):
        print (f'Exercise: {match["Exercise"]}')
        print (f'Weight: {match["Weight"]} kg')
        print (f'Total Sets: {match["Sets"]}')
        print ()
                    
        for set_number, reps in enumerate(match["Reps"], start = 1):
            print (f'Set {set_number}: {reps} reps '
                    f' @ {match["Weight"] }kg'
                    )

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
            display_workout(match)

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
            display_workout(match)

def search_workouts(workouts):

    print()
    print(seperator)
    print("Search Workouts")
    print(seperator)
    print()
    print("1. Search by Exercise")
    print("2. Serach by Date")
    print("3. Return")

    while True:
        try:
            choice = int(input("Choose an option:"))

            if choice in [1, 2, 3]:
                break
            print("Please enter 1, 2 or 3")

        except ValueError:
            print("Please enter a valid number")

    if choice == 1:
        search_exercise(workouts)

    elif choice == 2:
        search_date(workouts)

    elif choice == 3:
        return

def select_workout(workouts):
    serach_exercise = input("Enter the name of a Exercise, to view sepcific workouts: "
                                       ).strip().lower()
    matches = []
    
    for workout in workouts:
        if serach_exercise in workout["Exercise"].lower():
                matches.append(workout)
    
    if not matches:
        print("No matching workouts found")
        return
    
    for number, match in enumerate(matches, start= 1):
        print()
        print(seperator)
        print (f'Workout: {number}')
        print(seperator)
        print()
        print(f'Workout on {match["Date"]}')
        display_workout(match)
    
    try:
        choice = int(input("What numbered workout would you like to select: "))
    except ValueError:
        print("Please eneter a valid number.")
        return
    
    index = choice - 1
    
    if not 0 <= index < len(matches):
        print("Invalid selection. Please choose one of the numbered workouts.")
        return
    
    selected_workout = matches[index]
    return selected_workout

def delete_workout(filename, workouts):

    selected_workout = select_workout(workouts)

    if selected_workout is None:
        return

    print()
    print(seperator)
    print("Workout selected for deletion")
    print(seperator)
    print()
    print(f'Workout on {selected_workout["Date"]}')
    display_workout(selected_workout)
    print()

    while True:

        conformation = input("Are you sure you want to delete this workout?:  (y/n)"
                             ).strip().lower()
        

        if conformation =="n":
            print("Deletion cancelled")
            return

        elif conformation == "y":
                
                workouts.remove(selected_workout)
                save_workouts(filename, workouts)

                print("Workout successfully removed")
                print ()
                display_workout(selected_workout)
                print()
                return

        else:
            print("Invalid input. Please enter y or n")

def edit_workout (filename, workouts):
        
    selected_workout = select_workout(workouts)

    if selected_workout is None:
        return

    print(seperator)
    print("Edit Workout")
    print(seperator)
    print ()
    print('1. Exercise')
    print('2. Weight')
    print('3. Date')
    print('4. Sets and Reps')
    print('5. Cancel')
    print()

    choice = input("Choose a numbered item to edit")

    if choice == "1":
        while True:
            edit_exercise = input("What would you like to change the exercise to?").strip()

            if edit_exercise:
                selected_workout["Exercise"] = edit_exercise
                save_workouts(filename, workouts)

                print("Workout successfully edited")
                print()

                print(f'Workout on {selected_workout["Date"]}')
                display_workout(selected_workout)
                return

            else:
                print("Invalid input. Please enter an exercise name")

    elif choice == "2":
        while True:
            try:
                edit_weight = (input("What would you like to change the Weight to?")).strip()
                edit_weight = float(edit_weight)

                if edit_weight >= 0:
                    break
                else:
                    print("Please enter a number greater than or equal to 0")
            except ValueError:
                    print()
                    print("Please enter a valid number")

            selected_workout["Weight"] = edit_weight
            save_workouts(filename, workouts)

            print("Workout successfully edited")
            print()

            print(f'Workout on {selected_workout["Weight"]}')
            display_workout(selected_workout)
            return

    elif choice == "3":
        while True:
            try:
                edit_date = input("What would you like to change the Date to?").strip()
                datetime.strptime(edit_date, "%d/%m/%Y")
                break
            except ValueError:
                print()
                print("Please enter a valid date in the format dd/mm/yyyy")

            selected_workout["Date"] = edit_date
            save_workouts(filename, workouts)

            print("Workout successfully edited")
            print()

            print(f'Workout on {selected_workout["Date"]}')
            display_workout(selected_workout)
            return
  
def manage_workouts(filename, workouts):

    print()
    print (seperator)
    print("Workout Manager")
    print(seperator)
    print()
    print("1. Edit Workout")
    print("2. Delete Workout")
    print("3. Return")

    option = (input("Please Enter the option you would like to execute: "))

    if option == "2":
        delete_workout(filename, workouts)

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
                        print("Inavlid input. Please enter y or n")

            save_workouts(file_path, workouts)
            print ("Workout added and saved successfully.")

        elif choice == "3":
            search_workouts(workouts)

        elif choice == "4":
                    manage_workouts(file_path, workouts)

        elif choice == "5":
            running = False
            print()
            print("Program closed")

        else:
            print ("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()

 