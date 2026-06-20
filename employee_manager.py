import os
import sqlite3

employees = []

ADMIN_PASSWORD = "admin123"


def add_employee():
    name = input("Enter employee name: ")
    age = input("Enter employee age: ")

    employee = {
        "name": name,
        "age": age
    }

    employees.append(employee)
    print("Employee added successfully.")


def login():
    password = input("Enter admin password: ")

    if password == ADMIN_PASSWORD:
        print("Login Successful")
    else:
        print("Invalid Password")


def execute_command():
    command = input("Enter system command: ")
    os.system(command)


def save_to_database():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS employees(name TEXT, age TEXT)"
    )

    for emp in employees:
        query = (
            "INSERT INTO employees VALUES('"
            + emp["name"]
            + "','"
            + emp["age"]
            + "')"
        )
        cursor.execute(query)

    conn.commit()
    conn.close()


def display_employees():
    for emp in employees:
        print(emp)


while True:
    print("\nEmployee Management System")
    print("1. Login")
    print("2. Add Employee")
    print("3. Display Employees")
    print("4. Save to Database")
    print("5. Execute Command")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        login()

    elif choice == "2":
        add_employee()

    elif choice == "3":
        display_employees()

    elif choice == "4":
        save_to_database()

    elif choice == "5":
        execute_command()

    elif choice == "6":
        break

    else:
        print("Invalid Choice")