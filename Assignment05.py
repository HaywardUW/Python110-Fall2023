# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Kyle Hayward,11/13/2023,Completed Script
# ------------------------------------------------------------------------------------------ #

# Import the JSON module
import json

# Defining the Data Constants
MENU: str = '''
--------Course Registration Menu--------
 Select from the following menu:
   1. Register a Student for a Course
   2. Show current data
   3. Save data to a file
   4. Exit the program
----------------------------------------
'''
FILE_NAME: str = "Enrollments.json"

# Defining the Data Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
file = None
menu_choice: str = ""
student_data: dict = {}
student_list: list = []

# Exception handling
try:
    # Read the contents of the JSON file
    file = open(FILE_NAME, 'r')
    # Load contents of the JSON file into student_list
    student_list = json.load(file)
    # Close the file
    file.close()
# Present an error if "Enrollments.json" does not exist
except FileNotFoundError as e:
    print("This file doesn't exist! "
          "\nCreating the file and opening!")
    print("The file has been created!")
    # Creates "Enrollments.json" if the file does not exist
    file = open(FILE_NAME, 'w')
# Catch all exception for unforeseen errors
except Exception as e:
    print("There was a generic error opening the document!")
    print(e, e.__doc__,
          e.__str__())
# Closes the file if it is not already closed
finally:
    if file.closed == False:
        print("Closing the file!")
        file.close()

while True:
    # Print the Course Registration Menu
    print(MENU)
    # Use 'menu_choice' variable to store user's selection
    menu_choice = input("Please make a menu selection: ")
    print()

    if menu_choice == "1":
        try:
            print('*' * 50)
            # Prompt the user for input
            student_first_name = input("Please enter the student's first name: ")
            # Validate first name contains letters only
            if not student_first_name.isalpha():
                raise ValueError("\nThe first name should only contain letters!")
            student_last_name = input("Please enter the student's last name: ")
            # Validate last name contains letters only
            if not student_last_name.isalpha():
                raise ValueError("\nThe last name should only contain letters!")
            course_name = input("Please enter the course name: ")
            # Validate user does not leave course name blank
            if not course_name:
                raise ValueError("\nYou did not enter any course information!")
            # Adding data to the dictionary
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            # Appending dictionary data to the student list
            student_list.append(student_data)
            print(f'\nYou have registered '
                  f'{student_data["FirstName"]} '
                  f'{student_data["LastName"]} for '
                  f'{student_data["CourseName"]}')
            print('*' * 50)
        # Formatting the ValueError to the 'e' variable
        except ValueError as e:
            print(e)
            print("---Technical Error Message---")
            print(e.__doc__)
            print(e.__str__())
        # Formatting the Exception error to the 'e' variable
        except Exception as e:
            print("A non-specific error has occurred!\n")
            print("---Technical Error Message---")
            print(e, e.__doc__,
                  e.__str__(),
                  type(e),
                  sep='\n')
        continue

    elif menu_choice == "2":
        print('*' * 50)
        print("The current data is: \n")
        # Loop through and print all the data in the student list
        for student in student_list:
            print(f'{student["FirstName"]}, '
                  f'{student["LastName"]}, '
                  f'{student["CourseName"]}!')
        print('*' * 50)
        continue

    elif menu_choice == "3":
        try:
            # Open "Enrollments.json" and writes the student list data to it
            file = open(FILE_NAME, "w")
            json.dump(student_list, file)
            file.close()
            print('*' * 50)
            print("The following data has been saved: \n")
            for student in student_list:
                print(f'{student["FirstName"]}, '
                      f'{student["LastName"]}, '
                      f'{student["CourseName"]}!')
            print('*' * 50)
        # Raising an exception to validate the JSON format
        except TypeError as e:
            print("Please check that the data is a valid JSON format!\n")
            print("--Technical Error Message--")
            print(e, e.__doc__,
                  type(e),
                  sep="\n")
        # Catch-all exception
        except Exception as e:
            print("---Technical Error Message---")
            print("Built-In Python Error Info: ")
            print(e, e.__doc__,
                  type(e),
                  sep='\n')

    # Close the program
    elif menu_choice == "4":
        break

    # Prompt the user to choose a valid menu option
    else:
        print("Please choose option 1, 2, 3, or 4!")

print('*' * 50)
# Inform the user that the program has ended
print("The program has ended!")
print('*' * 50)

