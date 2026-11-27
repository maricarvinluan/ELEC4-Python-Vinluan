# Name: Maricar Untalan Vinluan
# Section: IV-BSIT A
# Activity: P4 - Safe Menu Program
# Date: November 22, 2026


def divide_numbers():
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        result = first_number / second_number

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")

    else:
        print("Result:", result)

    finally:
        print("Division operation finished.")


def read_file():
    try:
        file_name = input("Enter file name: ").strip()

        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print("Error! File not found.")

    except OSError:
        print("Error! Unable to open the file.")

    except UnicodeError:
        print("Error! Unable to read the file contents.")

    else:
        print("\n==== FILE CONTENTS ====")
        print(content)

    finally:
        print("File operation finished.")


def main():
    print("Name: Maricar Untalan Vinluan")
    print("Section: IV-BSIT A")

    while True:
        print("\n==== SAFE MENU PROGRAM ====")
        print("1. Divide Numbers")
        print("2. Read a File")
        print("3. Exit")

        try:
            choice = int(input("Choose an option: "))

            if choice == 1:
                divide_numbers()

            elif choice == 2:
                read_file()

            elif choice == 3:
                print("Thank you for using Safe Menu Program!")
                break

            else:
                print("Invalid menu selection! Choose 1, 2, or 3.")

        except ValueError:
            print("Invalid input! Please enter a number.")

        finally:
            print("Menu operation finished.")


main()