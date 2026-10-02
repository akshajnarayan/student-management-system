import core

def collect():
    name = input("Name : ").strip().lower()
    roll_no = int(input("Roll number : "))
    age = int(input("Age : "))
    standard = int(input("Standard : "))
    division = input("Division : ").strip()
    
    return roll_no, name, age, standard, division

def print_details(students, roll_no):
    name, age, standard, division = core.obtain(students, roll_no)
    
    print("Roll number : ", roll_no)
    print("Name : ", name.title())
    print("Age : ", age)
    print("Standard : ", standard)
    print("Division : ", division, "\n")

def add_student(students):
    print("\n----- Student Registration -----")
    try:
        roll_no, name, age, standard, division = collect()
    except ValueError:
        print("\nPlease enter a numeric value!")
        return
    
    if roll_no in students:
        print("\nA student with this roll number already exists!")
        return
    
    core.add_student(students, roll_no, name, age, standard, division)
    print("\nRegistered student details successfully.")

def view_students(students):
    print("\n----- Student Records -----\n")
    if not students:
        print("\nSorry, no student data found!")
        return
    
    for roll_no in students:
        print_details(students, roll_no)

def search_student(students):
    print("\n----- Search Student -----")
    if not students:
        print("\nSorry, no student data found!")
        return

    try:
        roll_no = int(input("Enter the roll number of the student : "))
    except ValueError:
        print("\nPlease enter a numeric value!")
        return
    
    if roll_no not in students:
        print("\nStudent not found!")
        return
    
    print("\n--- Student Details ---")
    print_details(students, roll_no)

def update_student(students):
    print("\n----- Update Student -----")
    if not students:
        print("\nSorry, no student data found!")
        return
    
    try:
        roll_no = int(input("Enter the roll number of the student : "))
    except ValueError:
        print("\nPlease enter a numeric value!")
        return
    
    if roll_no not in students:
        print("\nSorry, student not found!")
        return
    
    print("\n--- Existing Details ---")
    print_details(students, roll_no)

    while True:
        print("\n--- Update Student ---")
        print("1. Name")
        print("2. Age")
        print("3. Standard")
        print("4. Division")
        print("5. Exit\n")

        option = input("Enter your choice (1-5) : ")

        if option == '5':
            print("\nReturning to main menu ...")
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

            if field_input == students[roll_no][field]:
                print(f"\n{field.capitalize()} is already set to that value.")
            else:
                core.update_student(option, students, roll_no, field_input, status="update")
                print(f"\nUpdated {field} of student successfully.")

def remove_student(students):
    print("\n----- Remove Student -----")
    if not students:
        print("\nSorry, no student data found!")
        return
    
    try:
        roll_no = int(input("Enter the roll number of the student : "))
    except ValueError:
        print("\nPlease enter a numeric value!")
        return

    if roll_no not in students:
        print("\nSorry, student not found!")
        return

    print("\n--- Student Details ---")
    print_details(students, roll_no)

    confirmation = input("\nProceed with the removal? (y/n) : ").strip().lower()
    result = core.remove_student(students, roll_no, confirmation)
    if result:
        print("\nRemoved student details successfully.")
    elif result is False:
        print("\nProcess cancelled. Aborting removal.")
    else:
        print("\nInvalid choice! Aborting removal.")
