# Name: Maricar Untalan Vinluan
# Section: IV-BSIT A
# Activity: P2 - Custom Module
# Date: November 22, 2026

import student_utils
from student_utils import calculate_average
from datetime import date


def main():
    grades = []

    print("Name: Maricar Untalan Vinluan")
    print("Section: IV-BSIT A")

    # Accept five grades from the user
    while len(grades) < 5:
        try:
            grade = float(input("Enter a grade: "))

            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Invalid grade! Enter a grade from 0 to 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    print("\n==== STUDENT GRADE REPORT ====")
    print("Date:", date.today())
    print("Grades:", grades)

    print("Average:", round(calculate_average(grades), 2))
    print("Highest Grade:", student_utils.get_highest(grades))
    print("Lowest Grade:", student_utils.get_lowest(grades))
    print("Status:", student_utils.check_pass_fail(grades))


main()