# Personal Mini-Toolkit
# Week 8 Final Project


# ==================================================
# TOOL 1: SIMPLE CALCULATOR
# ==================================================
# This tool performs basic calculations using two numbers.
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        operation = input("Enter your choice: ")

        if operation == "1":
            answer = first_number + second_number
            print(f"Result: {first_number} + {second_number} = {answer}")

        elif operation == "2":
            answer = first_number - second_number
            print(f"Result: {first_number} - {second_number} = {answer}")

        elif operation == "3":
            answer = first_number * second_number
            print(f"Result: {first_number} x {second_number} = {answer}")

        elif operation == "4":
            if second_number == 0:
                print("Sorry, you cannot divide by zero.")
            else:
                answer = first_number / second_number
                print(f"Result: {first_number} / {second_number} = {answer}")

        else:
            print("Sorry, that is not a valid operation.")

    except ValueError:
        print("Please enter valid numbers.")


# ==================================================
# TOOL 2: TO-DO LIST
# ==================================================
# This tool allows the user to add, view, and remove tasks.
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"Task added: {task}")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour Tasks:")

                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                print("\nYour Tasks:")

                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(
                        input("Enter the task number to remove: ")
                    )

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Removed task: {removed_task}")
                    else:
                        print("That task number does not exist.")

                except ValueError:
                    print("Please enter a valid task number.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


# ==================================================
# TOOL 3: NUMBER CHECKER
# ==================================================
# This tool checks whether a number is positive, negative, or zero.
def number_checker():
    print("\n--- Number Checker ---")

    try:
        number = float(input("Enter a number: "))

        if number > 0:
            print(f"{number} is a positive number.")

        elif number < 0:
            print(f"{number} is a negative number.")

        else:
            print(f"{number} is zero.")

    except ValueError:
        print("Please enter a valid number.")


# ==================================================
# MAIN PROGRAM
# ==================================================
# This loop keeps showing the menu until the user chooses Quit.

print("========================================")
print("       WELCOME TO MY MINI-TOOLKIT")
print("========================================")
print("Choose from the available tools below.")

while True:
    print("\n========================================")
    print("              MAIN MENU")
    print("========================================")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Checker")
    print("4. Quit")
    print("========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        calculator()

    elif choice == "2":
        todo_list()

    elif choice == "3":
        number_checker()

    elif choice == "4":
        print("\nThank you for using my Personal Mini-Toolkit!")
        print("Goodbye! Have a great day.")
        break

    else:
        print("\nSorry, that is not a valid choice.")
        print("Please choose 1, 2, 3, or 4.")