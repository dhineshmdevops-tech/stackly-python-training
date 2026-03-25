employees = []
[
    {"name":"dhinesh", "age": 21,"role": "Devops","salary": 25000}
]
def add_employee():
    name = input("enter name: ")
    age = int(input("enter age: "))
    role = input("enter role: ")
    salary = int(input("enter salary: "))

    emp = {
        "name": name,
        "age": age,
        "role": role,
        "salary": salary
    }

    employees.append(emp)
    print("employee added successfully!")

def display_employees():
    if len(employees) == 0:
         print("no employees found")
    else:
        for emp in employees:
             print(emp)

def update_employee():
    name = input("enter employee name to update: ")

    for emp in employees:
        if emp ["name"] == name:
            emp["salary"] = float(input("enter new salary: "))
            print("employee updated!")
            return
        
    print("employee not found")

def delete_employee():
    name = input("Enter employee name to delete: ")

    for emp in employees:
        if emp["name"] == name:
            employees.remove(emp)
            print("employee deleted!")
            return

    print("employee not found")   

while True:
    print("\n1. Add Employee")
    print("2. Display Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        display_employees()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        break
    else:
        print("Invalid choice")

