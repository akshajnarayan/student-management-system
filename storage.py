import json

def load():
    try:
        with open("students.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError: 
        return None
    else:
        return {int(key):value for key, value in data.items()}
    
def store(data):
    with open("students.json", "w") as file:
        json.dump(data, file, indent=2)
