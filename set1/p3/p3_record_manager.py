# Name: Maricar Untalan Vinluan
# Section: IV-BSIT A
# Activity: P3 - Student Record Manager
# Date: November 22, 2026


def add_student(students):
    name = input("Enter student name: ").strip()

    if name == "":
        print("Name cannot be empty.")
    elif name.lower() in {student.lower() for student in students}:
        print("Student already exists!")
    else:
        students.append(name)
        print(name, "has been added successfully!")


def remove_student(students):
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.lower() == name.lower():
            students.remove(student)
            print(student, "has been removed successfully!")
            return

    print("Student not found.")


def search_student(students):
    name = input("Enter name to search: ").strip().lower()
    matches = []

    for student in students:
        if name in student.lower():
            matches.append(student)

    if len(matches) > 0:
        print("\nSearch Results:")
        for student in matches:
            print("-", student)
    else:
        print("No matching student found.")


def display_students(students):
    if len(students) == 0:
        print("No student records available.")
    else:
        print("\n==== STUDENT LIST ====")

        sorted_students = sorted(students, key=str.lower)

        for number, student in enumerate(sorted_students, start=1):
            print(number, ".", student)

        print("Total Students:", len(students))


def main():
    print("Name: Maricar Untalan Vinluan")
    print("Section: IV-BSIT A")

    students = []

    while True:
        print("\n==== STUDENT RECORD MANAGER ====")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display Students")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            remove_student(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            display_students(students)

        elif choice == "5":
            print("Thank you for using Student Record Manager!")
            break

        else:
            print("Invalid choice! Please try again.")


main()


# List vs Set:
# A list stores multiple items and keeps their order.
# A list can also contain duplicate values.
# A set stores unique values and does not allow duplicates.
# This program uses a list to store student names.
# A set is used to check for duplicate names before adding a student.