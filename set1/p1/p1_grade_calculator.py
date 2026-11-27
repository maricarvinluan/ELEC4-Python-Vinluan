# Name: Maricar Untalan Vinluan
# Section: IV-BSIT A
# Activity: P1 - Student Grade Calculator
# Date: November 18, 2026

PASSING_GRADE = 75


def enter_grades():
    grades = []

    while True:
        try:
            number_of_grades = int(input("How many grades will you enter? "))

            if number_of_grades > 0:
                break
            else:
                print("Please enter a number greater than 0.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    count = 0

    while count < number_of_grades:
        try:
            grade = float(input("Enter a grade: "))

            if grade >= 0 and grade <= 100:
                grades.append(grade)
                count += 1
            else:
                print("Invalid grade! Enter a grade from 0 to 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    return grades


def calculate_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)


def get_status(grades):
    average = calculate_average(grades)

    if average >= PASSING_GRADE:
        return "PASSED"
    else:
        return "FAILED"


def view_results(grades):
    if len(grades) == 0:
        print("No grades available. Please enter grades first.")
    else:
        print("\n==== STUDENT RESULTS ====")
        print("Grades entered:", grades)
        print("Average:", round(calculate_average(grades), 2))
        print("Highest Grade:", get_highest(grades))
        print("Lowest Grade:", get_lowest(grades))
        print("Status:", get_status(grades))


def main():
    grades = []

    while True:
        print("\n==== GRADE CALCULATOR ====")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            grades = enter_grades()

        elif choice == "2":
            view_results(grades)

        elif choice == "3":
            print("Thank you for using Grade Calculator!")
            break

        else:
            print("Invalid menu choice! Please try again.")


main()


# Local and Global Variables:
# PASSING_GRADE is a global variable because it is declared outside the functions.
# It is used by the get_status() function to determine if a student passed or failed.
# The grades variable inside enter_grades() is local because it is declared inside that function.
# Local variables are only accessible within the function where they are declared.
