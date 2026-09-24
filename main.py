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

students = {}

while True:    
    print("\n=========================================")
    print("\tStudent Management System\t")
    print("=========================================\n")

    print("1. Add Students")
    print("2. View Students")
    print("3. Search Students")
    print("4. Update Students")
    print("5. Delete Students")
    print("6. Exit\n")

    choice = input("Enter your choice (1-6) : ")

    match(choice):
        case '1':
            print()
            add_student()
        case '2':
            pass
        case '3':
            pass
        case '4':
            pass
        case '5':
            pass
        case '6':
            print("\nTerminating program, Please wait...")
            break
