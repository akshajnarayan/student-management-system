def obtain(students, student_id):
    name = students[student_id]["name"]
    age = students[student_id]["age"]
    standard = students[student_id]["standard"]
    division = students[student_id]["division"]  

    return name, age, standard, division

def add_student(students, student_id, name, age, standard, division):
    students[student_id] = {
        "name":name, 
        "age":age, 
        "standard":standard, 
        "division":division
    }

def update_student(option, students=None, student_id=None, field_input=None, status="update"):
    options = {
    '1': ("name", str),
    '2': ("age", int),
    '3': ("standard", int),
    '4': ("division", str)
    }
    if status == "init":
        return options[option]
    else:
        field = options[option][0]
        students[student_id][field] = field_input

def remove_student(students, student_id, confirmation):
    if confirmation in ('y', 'yes'):
        del students[student_id]
        return True
    elif confirmation in ('n', 'no'):
        return False
    else:
        return None