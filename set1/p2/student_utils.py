
# Name: Maricar Untalan Vinluan
# Section: IV-BSIT A
# Activity: P2 - Custom Module
# Date: November 22, 2026

PASSING_GRADE = 75


def calculate_average(grades):
    return sum(grades) / len(grades)


def check_pass_fail(grades):
    average = calculate_average(grades)

    if average >= PASSING_GRADE:
        return "PASSED"
    else:
        return "FAILED"


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)
