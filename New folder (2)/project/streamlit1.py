import streamlit as st 
from Correct_info_page import *
import os 
import json
import csv
import re
import pandas as pd

load_data()

st.title("Profile Catalogue💻..")
st.subheader("Manage your profile or see the information...")

menu=["Add Profile","View All","Delete by Phone number","truncate all"]
choice=st.sidebar.selectbox("Select action",menu)

if choice == "Add Profile":
    st.subheader("Add New Profile")

    name = st.text_input("Name").strip().lower()
    phone = st.text_input("Phone (10 digits)")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Save Profile"):
        if len(phone) != 10 or not phone.isdigit():
            st.error("Invalid phone number")
        elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            st.error("Invalid email")
        else:
            issues = check_password_strength(password)
            if issues:
                st.warning("Weak password:")
                for issue in issues:
                    st.write("-", issue)
            else:
                with open(file, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    if any(row["Name"].lower() == name for row in reader):
                        st.warning("Name already exists!")
                    else:
                        with open(file, 'a', newline='', encoding='utf-8') as f:
                            writer = csv.writer(f)
                            writer.writerow([name, phone, email])
                        save_password(name, password)
                        st.success("Profile saved successfully ✅")        
elif choice == "View All":
    if os.path.exists(file):
        df = pd.read_csv(file)
        st.dataframe(df)
    else:
        st.info("No profiles found.") 
elif choice == "Delete by Phone number":
    number = st.text_input("Enter Phone number to Delete").strip()
    name_to_delete=None
    if st.button("Delete"):
        found = False
        with open(file, 'r', encoding='utf-8') as f:
           with open(file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = []
            for row in reader:
                if row["Phone"] == number:
                    found = True
                    name_to_delete = row["Name"].lower()
                    continue 
                rows.append(row)
        with open(file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["Name", "Phone", "Email"])
            writer.writeheader()
            writer.writerows(rows)
        with open(secured_data, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if name_to_delete in data:
            found = True
            del data[name_to_delete]
        with open(secured_data, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

        if found:
            st.success(f"Deleted record: {name_to_delete}")
        else:
            st.warning(f"No record found for {name_to_delete}")
elif choice == "truncate all":
    if st.button("Confirm Delete All..?"):
        truncate_all()
        st.success("All data cleared! ✅")                           