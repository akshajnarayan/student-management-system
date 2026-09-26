def details_of(rollno):
    name = students[rollno]["name"]
    age = students[rollno]["age"]
    standard = students[rollno]["standard"]
    division = students[rollno]["division"]

    return name, age, standard, division

def add_student():
    print("----- Student Registration -----")
    try:
        name = input("Name : ").strip().lower()
        roll_no = int(input("Roll number : "))
        age = int(input("Age : "))
        standard = int(input("Standard : "))
        division = input("Division : ").strip()
    except ValueError:
        print("\nPlease enter a numeric value!")
    else:
        if roll_no in students:
            print("\nA student with this roll number already exists!")
        else:
            students[roll_no] = {"name":name, "age":age, "standard":standard, "division":division}
            print("\nRegistered student details successfully.")

def view_students():
    if not students:
        print("Sorry, no student data found!")
        return
    
    print("----- Student Records -----\n")
    for roll_no, details in students.items():
        print("Roll number : ", roll_no)
        print("Name : ", details["name"].capitalize())
        print("Age : ", details["age"])
        print("Standard : ", details["standard"])
        print("Division : ", details["division"], "\n")

def search_student():
    if not students:
        print("Sorry, no student data found!")
        return
    try:
        roll_no = int(input("Enter the roll number of the student : "))
    except ValueError:
        print("\nPlease enter a numeric value!")
    else:
        if roll_no not in students:
            print("\nStudent not found!")
        else:
            name, age, standard, division = details_of(roll_no)
            print("\n----- Student Details -----")
            print("Name : ", name.capitalize())
            print("Roll Number : ", roll_no)
            print("Age : ", age)
            print("Standard : ", standard)
            print("Division : ", division)

def update_student():
    options = {
        '1': ("name", str),
        '2': ("age", int),
        '3': ("standard", int),
        '4': ("division", str)
    }

    print("----- Update Student -----")

    try:
        roll_no = int(input("Enter the roll number of the student : "))
    except ValueError:
        print("\nPlease enter a numeric value!")
        return

    if roll_no not in students:
        print("\nSorry, student not found!")
        return

    name, age, standard, division = details_of(roll_no)

    print("\n--- Existing Details ---")
    print("Name : ", name.capitalize())
    print("Roll Number : ", roll_no)
    print("Age : ", age)
    print("Standard : ", standard)
    print("Division : ", division)

    while True:
        print("\n--- Update Student ---")
        print("1. Name")
        print("2. Age")
        print("3. Standard")
        print("4. Division")
        print("5. Exit\n")

        option = input("Enter your choice (1-5) : ")
        print()

        if option in ('1', '2', '3', '4'):
            field, datatype = options[option]
            try:
                user_input = datatype(input(f"Enter {field} : "))
            except ValueError:
                print("\nPlease enter a numeric value!")
            else:
                if datatype == str:
                    user_input = user_input.strip().lower()

                if user_input == students[roll_no][field]:
                    print(f"\n{field.capitalize()} is already set to that value.")
                else:
                    students[roll_no][field] = user_input

                    print(f"\nUpdated {field} of student successfully.")
        elif option == '5':
            print("\nReturning to main menu ...")
            break
        else:
            print("\nInvalid choice! Try again.")

def remove_student():
    print("----- Remove Student -----")
    try:
        roll_no = int(input("Enter the roll number of the student : "))
    except ValueError:
        print("\nPlease enter a numeric value!")
        return

    if roll_no not in students:
        print("\nSorry, student not found!")
        return

    name, age, standard, division = details_of(roll_no)

    print("\n--- Student Details ---")
    print("Name : ", name.capitalize())
    print("Roll Number : ", roll_no)
    print("Age : ", age)
    print("Standard : ", standard)
    print("Division : ", division)

    confirmation = input("\nProceed with the removal? (y/n) : ").strip().lower()
    if confirmation in ('y', 'yes'):
        del students[roll_no]
        print("\nRemoved student details successfully.")
    elif confirmation in ('n', 'no'):
        print("\nAborting removal.")
    else:
        print("Invalid choice! Aborting removal.")

students = {}

while True:    
    print("\n=========================================")
    print("\tStudent Management System\t")
    print("=========================================\n")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Remove Student")
    print("6. Exit\n")

    choice = input("Enter your choice (1-6) : ")

    match(choice):
        case '1':
            print()
            add_student()
        case '2':
            print()
            view_students()
        case '3':
            print()
            search_student()
        case '4':
            print()
            update_student()
        case '5':
            print()
            remove_student()
        case '6':
            print("\nTerminating program, Please wait...")
            break
        case _:
            print("Invalid choice! Try again.")
