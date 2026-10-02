import ui
import storage

students = storage.load()
if students is None:
    print("\nFailed to import student records! : File Not Found")
    exit()

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
            ui.add_student(students)
            storage.store(students)
        case '2':
            ui.view_students(students)
        case '3':
            ui.search_student(students)
        case '4':
            ui.update_student(students)
            storage.store(students)
        case '5':
            print()
            ui.remove_student(students)
            storage.store(students)
        case '6':
            print("\nTerminating program, Please wait...")
            break
        case _:
            print("Invalid choice! Try again.")
