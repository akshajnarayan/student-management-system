import core
import animations

def collect():
    name = input("Name : ").strip().lower()
    student_id = input("Student ID : ")
    age = int(input("Age : "))
    standard = int(input("Standard : "))
    division = input("Division : ").strip()
    
    return student_id, name, age, standard, division

def print_details(students, student_id):
    name, age, standard, division = core.obtain(students, student_id)
    
    print("Student ID : ", student_id)
    print("Name : ", name.title())
    print("Age : ", age)
    print("Standard : ", standard)
    print("Division : ", division, "\n")

def add_student(students):
    print("\n----- Student Registration -----")
    try:
        student_id, name, age, standard, division = collect()
    except ValueError:
        print("\nPlease enter a numeric value!")
        return

    if not student_id.isalnum():
        print("\nInvalid ID! Special characters are not allowed.")
        return

    if student_id.isdigit():
        print("\nInvalid ID! IDs must contain letters and numbers.")
        return 
    
    if not student_id.isupper():
        print("\nInvalid ID! Inappropriate case.")
        return

    if any(char.isdigit() for char in name):
        print("\nStudent name cannot contain integers.")
        return

    if student_id in students:
        print("\nA student with this Student ID already exists!")
        return

    animations.spinner(text="Saving student details", end="")
    core.add_student(students, student_id, name, age, standard, division)
    print("\nRegistered student successfully.")

def view_students(students):
    print("\n----- Student Records -----\n")
    animations.loading(text="Loading students data", loop=1, dots=5, end="")
    if not students:
        print("Sorry, no student data found!")
        return
    
    for student_id in students:
        print_details(students, student_id)

def search_student(students):
    print("\n----- Search Student -----")
    animations.loading(text="Loading students data", loop=1, dots=5, end="")
    if not students:
        print("\nSorry, no student data found!")
        return

    student_id = input("Enter the Student ID of the student : ")

    if not student_id.isalnum():
        print("\nInvalid ID! Special characters are not allowed.")
        return

    if student_id.isdigit():
        print("\nInvalid ID! IDs must contain letters and numbers.")
        return
    
    if not student_id.isupper():
        print("\nInvalid ID! Inappropriate case.")
        return

    animations.spinner(text="Fetching student details", end="")
    if student_id not in students:
        print("\nStudent not found!")
        return
    
    print("\n--- Student Details ---")
    print_details(students, student_id)

def update_student(students):
    print("\n----- Update Student -----")
    animations.loading(text="Loading students data", loop=1, dots=5, end="")
    if not students:
        print("\nSorry, no student data found!")
        return
    
    student_id = input("Enter the Student ID of the student : ")

    if not student_id.isalnum():
        print("\nInvalid ID! Special characters are not allowed.")
        return

    if student_id.isdigit():
        print("\nInvalid ID! IDs must contain letters and numbers.")
        return

    if not student_id.isupper():
        print("\nInvalid ID! Inappropriate case.")
        return

    animations.spinner(text="Fetching student details", end="")
    if student_id not in students:
        print("\nSorry, student not found!")
        return
    
    print("\n--- Existing Details ---")
    print_details(students, student_id)

    while True:
        print("--- Update Student ---")
        print("1. Name")
        print("2. Age")
        print("3. Standard")
        print("4. Division")
        print("5. Exit\n")

        option = input("Enter your choice (1-5) : ")

        if option == '5':
            animations.loading(text="Saving changes", display="\nReturning to main menu")
            return
        if option not in ('1', '2', '3', '4'):
            print("\nInvalid choice! Try again.")
        else:
            field, datatype = core.update_student(option, status="init")
            try:
                field_input = datatype(input(f"\nEnter new {field} : "))
            except ValueError:
                print("\nPlease enter a numeric value!")
                return 
            
            if datatype == str:
                field_input = field_input.strip().lower()

            if field == "name" and any(char.isdigit() for char in field_input):
                print("\nStudent name cannot contain integers.")
                return 
            
            if field_input == students[student_id][field]:
                print(f"\n{field.capitalize()} is already set to that value.")
            else:
                core.update_student(option, students, student_id, field_input, status="update")
                print(f"\nUpdated {field} of student successfully.\n")

def remove_student(students):
    print("\n----- Remove Student -----")
    animations.loading(text="Loading students data", loop=1, dots=5, end="")
    if not students:
        print("\nSorry, no student data found!")
        return
    
    student_id = input("Enter the Student ID of the student : ")

    if not student_id.isalnum():
        print("\nInvalid ID! Special characters are not allowed.")
        return

    if student_id.isdigit():
        print("\nInvalid ID! IDs must contain letters and numbers.")
        return

    if not student_id.isupper():
        print("\nInvalid ID! Inappropriate case.")
        return

    animations.spinner(text="Fetching student details", end="")
    if student_id not in students:
        print("\nSorry, student not found!")
        return

    print("\n--- Student Details ---")
    print_details(students, student_id)

    confirmation = input("\nProceed with the removal? (y/n) : ").strip().lower()
    result = core.remove_student(students, student_id, confirmation)
    if result:
        animations.spinner(text="Removing student details", end="")
        print("\nRemoved student details successfully.")
    elif result is False:
        print("\nProcess cancelled. Aborting removal.")
    else:
        print("\nInvalid choice! Aborting removal.")
