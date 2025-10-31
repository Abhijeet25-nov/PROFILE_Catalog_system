import os
import json
import csv
import re

file = "Login_info.csv"
secured_data = "ID_PASS.json"

def load_data():
    if not os.path.exists(file):
        with open(file, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Phone", "Email"])
    if not os.path.exists(secured_data):
        with open(secured_data, "w", encoding="utf-8") as f:
            json.dump({}, f)

def save_password(name, password):
    with open(secured_data, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    data[name] = password
    with open(secured_data, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def check_password_strength(password):
    issues = []
    if len(password) < 7:
        issues.append("Too short (min 7 chars)")
    if not any(c.islower() for c in password):
        issues.append("Missing lowercase")
    if not any(c.isupper() for c in password):
        issues.append("Missing uppercase")
    if not any(c.isdigit() for c in password):
        issues.append("Missing digit")
    if not any(c in "!@#$%^&*()" for c in password):
        issues.append("Missing special char")
    return issues

def detail_entry():
    name = input("Enter name: ").strip().lower()
    with open(file, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Name"].lower() == name:
                print("Name already exists")
                return
    while True:
        phone_no = input("Enter phone number: ").strip()
        if len(phone_no) != 10 or not phone_no.isdigit():
            print("❌ Invalid phone number")
            continue
        else:
            break
    while True:    
        email_id = input("Enter email: ").strip()
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email_id):
            print("❌ Invalid email")
            continue
        else:
            break
        
    while True:    
        password = input("Enter password: ").strip()
        issues = check_password_strength(password)
        if issues:
            print("Weak password:", ", ".join(issues))
            print("Can't save..")
            continue
        else:
            break
    save_password(name, password)
    print("✅Password saved successfully!")
        
    
    with open(file, 'a', encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, phone_no, email_id])

    print("✅ Details saved successfully!")

def truncate_all():
    with open(file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])
    with open(secured_data, 'w', encoding='utf-8') as f:
        json.dump({}, f)
    print("All data cleared..✅")

def truncate_data():
    name = input("Enter the name you want to delete: ").lower()
    found = False
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = [row for row in reader if row["Name"].lower() != name]

        total_rows = len(rows)
        if total_rows < sum(1 for _ in open(file, 'r', encoding='utf-8')) - 1:
            found = True

        with open(file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["Name", "Phone", "Email"])
            writer.writeheader()
            writer.writerows(rows)
    if os.path.exists(secured_data):
        with open(secured_data, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if name in data:
            found = True
            del data[name]

        with open(secured_data, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    if found:
        print(f"✅ This name: {name} deleted successfully!")
    else:
        print(f"No name found: {name}.")
        
def main():
    load_data()
    while True:
        print("1. Add new profile")
        print("2. Truncate all data")
        print("3. Truncate by name")
        print("4. Exit")
        choice = input("Choose: ").strip()
        match choice:
            case '1': detail_entry()
            case '2': truncate_all()
            case '3': truncate_data()
            case '4': break
            case _: print("Invalid choice")

if __name__ == "__main__":
    main()