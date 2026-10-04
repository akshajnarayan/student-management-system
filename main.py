import ui
import time
import storage
import animations

animations.import_data(texts=("Locating database", "Fetching student records", "Just a moment"))
students = storage.load()

if students is None:
    print("Failed to import : Student records not found.")
    exit()

print("Import successful.", end="", flush=True)

time.sleep(1)
print("\r\033[2K", end="")
        

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
            animations.progress_bar(filler="-", display="\n|----- End of program -----|")
            break
        case _:
            print("Invalid choice! Try again.")
