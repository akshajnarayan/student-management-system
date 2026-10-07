import json

def load(filename="students.json"):
    try:
        with open(f"data/{filename}", "r") as file:
            data = json.load(file)
    except FileNotFoundError: 
        return None
    else:
        return {key:value for key, value in data.items()}
    
def store(data, filename="students.json"):
    with open(f"data/{filename}", "w") as file:
        json.dump(data, file, indent=2)
