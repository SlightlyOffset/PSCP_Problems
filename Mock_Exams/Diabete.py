import re
import json

def data_extraction(literal_string: str):
    '''Extract all data out from input string using re'''
    pattern = r'\{[^}]*"name":\s*"([^"]+)",\s*"age":\s*([\d.]+),\s*"sugar":\s*([\d.]+)[^}]*\}'
    return re.findall(pattern, literal_string)

def check_sugar_intake(person: dict):
    '''Check if a person's sugar intake exceeds the recommended limit'''
    age = person.get("age")
    sugar = person.get("sugar")

    if age is None or sugar is None or age < 6:
        person["error"] = True
        return person

    if 6 <= age <= 13:
        person["exceeds_limit"] = sugar > 16
    elif 14 <= age < 25:
        person["exceeds_limit"] = sugar > 24
    elif 25 <= age < 60:
        person["exceeds_limit"] = sugar > 16
    elif age >= 60:
        person["exceeds_limit"] = sugar > 16
    else:
        person["error"] = True

    return person

def main():
    '''Main logic'''
    data = input()
    extracted_data = data_extraction(data)

    people = []
    for name, age, sugar_level in extracted_data:
        people.append({
            "name": name,
            "age": float(age),
            "sugar": float(sugar_level),
            "exceeds_limit": False,
            "error": False
        })

    exceed_count = 0
    not_exceed_count = 0

    for person in people:
        result = check_sugar_intake(person)
        age_display = int(result["age"])
        name = result["name"]

        if result["error"]:
            print(f"{name} ({age_display}): error")
        elif result["exceeds_limit"]:
            exceed_count += 1
            print(f"{name} ({age_display}): eat too much sugar")
        else:
            not_exceed_count += 1
            print(f"{name} ({age_display}): eat sugar within the limit")

    print("\nExceed:", exceed_count)
    print("Not Exceed:", not_exceed_count)

if __name__ == "__main__":
    main()
