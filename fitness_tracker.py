import csv
from datetime import datetime
import ast

separator = "=" * 50

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

        print(separator)
        print(f'Workout on {date}')
        print(separator)

        for workout in daily_workouts:
            display_workout(workout)

def get_sets_and_reps():
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

    return total_sets, reps 

def add_workout(workouts):

    while True:
        date = input(
            "What was the date of this workout? (dd/mm/yyyy):\n"
        ).strip()

        try:
            datetime.strptime(date, "%d/%m/%Y")
            break

        except ValueError:
            print(
                "Please enter a valid date "
                "in the format dd/mm/yyyy."
            )

    while True:
        exercise = input(
            "What exercise did you complete?:\n"
        ).strip().title()

        if exercise:
            break

        print("Please enter an exercise name.")

    while True:
        try:
            weight = float(input('What weight did you use (kg)?: \n'))
            if weight >= 0:
                break

            else:
                print("Please enter a number greater than or equal to 0")

        except ValueError:
            print()
            print("Please enter a valid number.")
           
    total_sets, reps = get_sets_and_reps()
            

    new_exercise = {"Date": date,
                    "Exercise": exercise,
                    "Weight": weight,
                    "Sets": total_sets,
                    "Reps": reps
                    }

    is_new_pr, previous_pr = check_weight_pr(workouts, new_exercise)

    workouts.append(new_exercise)

    if previous_pr is None:
        print()
        print(separator)
        print("🏆 FIRST RECORDED PERFORMANCE!")
        print(separator)
        print()
        print(f'Exercise: {new_exercise["Exercise"]}')
        print()
        print(f'Weight: {new_exercise["Weight"]} kg')
        print()
        print("Great start! This is your first personal record for this exercise, time to build on this! 💪")

    elif is_new_pr:
            
        improvement = new_exercise["Weight"] - previous_pr

        print()
        print(separator)
        print("🏆 NEW PERSONAL RECORD!")
        print(separator)
        print()
        print(f'Exercise: {new_exercise["Exercise"]}')
        print()
        print(f'Previous best: {previous_pr} kg')
        print(f'New best: {new_exercise["Weight"]} kg')
        print(f'Improvement: {improvement} kg')
        print()
        print("Fantastic work! Keep pushing! 💪")

    return workouts

def show_menu():
      print(separator)
      print("Fitness Progress Coach".center(50))
      print(separator)
      print ()
      print('1. View Workouts')
      print('2. Add Workout')
      print('3. Search Workouts')
      print('4. Personal Records')
      print('5. Manage Workouts')
      print('6. Exit')
      print()

def display_workout(match):
        print (f'Exercise: {match["Exercise"]}')
        print (f'Weight: {match["Weight"]} kg')
        print (f'Total Sets: {match["Sets"]}')
        print ()
                    
        for set_number, reps in enumerate(match["Reps"], start = 1):
            print (f'Set {set_number}: {reps} reps '
                    f' @ {match["Weight"]} kg'
                    )

def search_date(workouts):
        
    while True:
        search_term = input(
            "Enter the date to view the corresponding workout: "
        ).strip()

        if search_term:
            break

        print("Please enter a date.")

    matches = []

    for workout in workouts:
        if search_term in workout["Date"]:
            matches.append(workout)

    if not matches:
            print()
            print ("No matching workout found for that date.")
            print()

    else:
        for match in matches:
            print ()
            print(separator)
            print(f'Workout on {match["Date"]}')
            print(separator)
            display_workout(match)

def search_exercise(workouts):
    
    while True:
        search_term = input(
            "Enter the name of an exercise "
            "to view previous stats: "
        ).strip().lower()

        if search_term:
            break

        print("Please enter an exercise name.")

    matches = []

    for workout in workouts:
        if search_term in workout["Exercise"].lower():
            matches.append(workout)

    if not matches:
            print()
            print ("No matching exercise found")
            print()

    else:
        for match in matches:
            print ()
            print(separator)
            print(f'Workout on {match["Date"]}')
            print(separator)
            display_workout(match)

def search_workouts(workouts):

    print()
    print(separator)
    print("Search Workouts")
    print(separator)
    print()
    print("1. Search by Exercise")
    print("2. Search by Date")
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

    while True:
        search_exercise = input("Enter the name of a exercise to view specific workouts: "
                                       ).strip().lower()

        if search_exercise:
            break

        print("Please enter an exercise name.")

    matches = []
    
    for workout in workouts:
        if search_exercise in workout["Exercise"].lower():
                matches.append(workout)
    
    if not matches:
        print("No matching workouts found")
        return
    
    for number, match in enumerate(matches, start= 1):
        print()
        print(separator)
        print (f'Workout: {number}')
        print(separator)
        print()
        print(f'Workout on {match["Date"]}')
        display_workout(match)

    while True:

        try:
            choice = int(
                input("What numbered workout would you like to select: ")
            )

            index = choice - 1

            if 0 <= index < len(matches):
                break

            print(
                "Invalid selection. "
                "Please choose one of the numbered workouts."
            )

        except ValueError:
            print("Please enter a valid whole number.")

    selected_workout = matches[index]
    return selected_workout

def delete_workout(filename, workouts):

    selected_workout = select_workout(workouts)

    if selected_workout is None:
        return

    print()
    print(separator)
    print("Workout selected for deletion")
    print(separator)
    print()
    print(f'Workout on {selected_workout["Date"]}')
    display_workout(selected_workout)
    print()

    while True:

        confirmation = input("Are you sure you want to delete this workout?:  (y/n)"
                             ).strip().lower()
        

        if confirmation =="n":
            print("Deletion cancelled")
            return

        elif confirmation == "y":
                
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

    while True:
        print(separator)
        print("Edit Workout")
        print(separator)
        print ()
        print('1. Exercise')
        print('2. Weight')
        print('3. Date')
        print('4. Sets and Reps')
        print('5. Cancel')
        print()

        choice = input("Choose a numbered item to edit: ")

        if choice == "1":

            while True:
                edit_exercise = input("What would you like to change the exercise to?: ").strip().title()

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
                    edit_weight = float(input(
                    "What would you like to change the weight to? "
                ).strip()
            )

                    if edit_weight < 0:
                        print(
                        "Please enter a number greater than "
                        "or equal to 0."
                        )
                        continue

                    break

                except ValueError:
                    print()
                    print("Please enter a valid number.")

            selected_workout["Weight"] = edit_weight
            save_workouts(filename, workouts)

            print()
            print("Workout successfully edited.")
            print(f'Workout on {selected_workout["Date"]}')
            display_workout(selected_workout)
            return

        elif choice == "3":
            while True:

                edit_date = input(
                        "What would you like to change the date to? "
                        ).strip()

                try:
                    datetime.strptime(edit_date, "%d/%m/%Y")
                    break

                except ValueError:
                    print()
                    print("Please enter a valid date in the format dd/mm/yyyy."
                            )

            selected_workout["Date"] = edit_date
            save_workouts(filename, workouts)

            print()
            print("Workout successfully edited.")
            print(f'Workout on {selected_workout["Date"]}')
            display_workout(selected_workout)
            return

        elif choice == "4":
            while True:

                edit_set = input ("Would you like to change the amount of sets?: (y/n)"
                                    ).strip().lower()
                    
                if edit_set == "y":
                        total_sets, reps = get_sets_and_reps()

                        selected_workout ["Sets"] = total_sets
                        selected_workout ["Reps"] = reps

                        save_workouts(filename, workouts)

                        print()
                        print("Workout successfully edited.")
                        print(f'Workout on {selected_workout["Date"]}')
                        display_workout(selected_workout)
                        return

                elif edit_set == "n":

                    while True:
                        edit_reps = input("Would you like to change the amount of reps completed in one or more sets?: (y/n)").strip().lower()

                        if edit_reps == "y":
                            break

                        elif edit_reps == "n":
                            print("Workout edit cancelled.")
                            return

                        else:
                            print("Invalid input. Please enter y or n")
                      
                    while True:
                                print(separator)
                                print("Edit Reps")
                                print(separator)

                                for set_number, reps in enumerate(
                                    selected_workout["Reps"],
                                    start=1
                                    ):
                                    print(f"{set_number}. Set {set_number}: {reps} reps")

                                return_option = len(selected_workout["Reps"]) + 1
                                print(f"{return_option}. Return")

                                try: 
                                    set_choice = int(input("Choose a set to edit: "))

                                except ValueError:
                                    print("Please enter a valid whole number.")
                                    continue

                                if set_choice == return_option:
                                    save_workouts(filename, workouts)

                                    print("Workout edited successfully")
                                    print()
                                    print(f'Workout on {selected_workout["Date"]}')
                                    display_workout(selected_workout)
                                    return
                                
                                else:
                                    set_index = set_choice - 1

                                    if 0 <= set_index < len(selected_workout["Reps"]):
                                        while True:

                                            try:
                                                new_reps = int(input("What is the new number of reps?: "))

                                                if new_reps > 0:
                                                    selected_workout["Reps"][set_index] = new_reps
                                                    print("Set updated successfully.")
                                                    break

                                                else:
                                                    print("Enter a number greater than 0")

                                            except ValueError:
                                                print("Please enter a valid whole number")

                                    else:
                                        print("Please choose one of the numbered options.")

                else:
                    print("Invalid input please select y or n")

        elif choice == "5":
            print("Workout edit cancelled")
            return

        else:
            print("Invalid option. Please choose 1, 2, 3, 4, or 5.")

def manage_workouts(filename, workouts):

    while True:
        print()
        print (separator)
        print("Workout Manager")
        print(separator)
        print()
        print("1. Edit Workout")
        print("2. Delete Workout")
        print("3. Return")

        option = (input(
            "Please Enter the option you would like to execute: "
            ).strip())

        if option == "1":
            edit_workout(filename, workouts)

        elif option == "2":
            delete_workout(filename, workouts)

        elif option == "3":
            return

        else:
            print("Invalid option. Please input 1, 2 or 3")

def calculate_weight_prs(workouts):

    weight_prs = {}

    for workout in workouts:
        exercise = workout["Exercise"]
        weight = workout["Weight"]

        if exercise not in weight_prs:
            weight_prs[exercise] = weight

        else:
            if weight_prs[exercise] < weight:
                weight_prs[exercise] = weight
    return weight_prs

def check_weight_pr(workouts, new_workout):

    exercise = new_workout["Exercise"]
    new_weight = new_workout["Weight"]

    current_prs = calculate_weight_prs(workouts)
    previous_pr = current_prs.get(exercise)

    if previous_pr is None:
        return True, None
    
    elif new_weight > previous_pr:
        return True, previous_pr

    else:
        return False, previous_pr

def view_personal_records(workouts):

    weight_prs = calculate_weight_prs(workouts)

    print()
    print(separator)
    print("Personal Records")
    print(separator)
    print()

    for exercise, weight in sorted(weight_prs.items()):

        print(exercise)
        print(f'Highest Weight: {weight} kg')
        print()

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
                    ).strip().lower()

                    if another_workout == "n":
                        adding_exercise = False
                        break

                    elif another_workout == "y":
                        break
                    
                    else:   
                        print("Invalid input. Please enter y or n")

            save_workouts(file_path, workouts)
            print ("Workout added and saved successfully.")

        elif choice == "3":
            search_workouts(workouts)

        elif choice == "4":
            view_personal_records(workouts)

        elif choice == "5":
            manage_workouts(file_path, workouts)

        elif choice == "6":
            running = False
            print()
            print("Program closed")

        else:
            print ("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()

 