def add_student():
    print("----- Student Registration -----")
    try:
        name = input("Name : ")
        roll_no = int(input("Roll number : "))
        age = int(input("Age : "))
        standard = int(input("Standard : "))
        division = input("Division : ")
    except ValueError:
        print("\nPlease enter a numeric value!")
    else:
        if roll_no in students:
            print("\nA student with this roll number already exists!")
        else:
            students[roll_no] = {"name":name.lower(), "age":age, "standard":standard, "division":division}
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
        roll_no = int(input("Enter the roll number of the student:"))
    except ValueError:
        print("\nPlease enter a numeric value!")
    else:
        if roll_no not in students:
            print("\nStudent not found!")
        else:
            print("\n----- Student Details -----")
            print("Name : ", students[roll_no]["name"].capitalize())
            print("Roll Number : ", roll_no)
            print("Age : ", students[roll_no]["age"])
            print("Standard : ", students[roll_no]["standard"])
            print("Division : ", students[roll_no]["division"])

students = {}

while True:    
    print("\n=========================================")
    print("\tStudent Management System\t")
    print("=========================================\n")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
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
            pass
        case '5':
            pass
        case '6':
            print("\nTerminating program, Please wait...")
            break
        case _:
            print("Invalid choice! Try again.")
