def obtain(students, roll_no):
    name = students[roll_no]["name"]
    age = students[roll_no]["age"]
    standard = students[roll_no]["standard"]
    division = students[roll_no]["division"]  

    return name, age, standard, division

def add_student(students, roll_no, name, age, standard, division):
    students[roll_no] = {
        "name":name, 
        "age":age, 
        "standard":standard, 
        "division":division
    }

def update_student(option, students=None, roll_no=None, field_input=None, status="update"):
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
        students[roll_no][field] = field_input

def remove_student(students, roll_no, confirmation):
    if confirmation in ('y', 'yes'):
        del students[roll_no]
        return True
    elif confirmation in ('n', 'no'):
        return False
    else:
        return None