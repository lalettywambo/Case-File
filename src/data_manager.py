import json


FILE_PATH = "data/users.json"


def save_detective(detective):
    try:
        with open(FILE_PATH, "r") as file:
            detectives = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        detectives = []

    detectives.append({
        "name": detective.name,
        "email": detective.email,
        "password": detective.password
    })

    with open(FILE_PATH, "w") as file:
        json.dump(detectives, file, indent=4)


def get_detectives():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


    
def get_cases():
    try:
        with open("data/cases.json", "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_record(case, suspect, result):
    try:
        with open("data/records.json", "r") as file:
            records = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        records = []

    records.append({
        "case_id": case["case_id"],
        "case_title": case["title"],
        "suspect": suspect,
        "result": result
    })

    with open("data/records.json", "w") as file:
        json.dump(records, file, indent=4)