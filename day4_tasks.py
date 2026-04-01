# MINI PROJECTS 

# Mini Project 1: Employee Management System

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

# Mini Project 2: Student Report Card

name = input("Enter student name: ")
marks = []
for i in range(1, 4):
    mark = float(input(f"enter mark for subject {i}: "))
    marks.append(mark)

total = sum(marks)
average = total / 3
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average>= 60:
    grade = 'C'
else:
    grade = 'D'

print("\n--- student report card ---")
print(f"name: {name}")
print(f"marks: subject 1 = {marks[0]}, subject 2 = {marks[1]}, subject 3 = {marks[2]}")
print(f"total:{total}")
print(f"average: {average:.2f}")
print(f"grade: {grade}")

# Mini Project 3: Shopping Cart System

cart = []

while True:
    print("\n1. add 2.remove 3.show 4.exit")
    choice = input("enter choice: ")

    if choice == "1":
        name = input("product name: ")
        price = float(input("price: "))
        qty = int(input("quantity: "))
        cart.append({"name": name, "price": price, "qty": qty})
        print("item added")

    elif choice == "2":
        name = input("enter product to remove: ")
        for item in cart:
            if item["name"] == name:
                cart.remove(item)
                print("removed")
                break
    elif choice == "3":
        total = 0
        for item in cart:
            price(item)
            total += item["price"] * item["qty"]
        print("total bill:", total)

    elif choice == "4":
        break

# Mini Project 4: Login & User Validation

users = {
    "dhinesh": "1234",
    "admin": "admin"
}
username = input("enter username: ")
password = input("enter password: ")

if username in users and users[username] == password:
    print("login successful")
else:
    print("invalid login")

# Mini Project 5: Unique Visitor Counter

visitors = set()

while True:
    name = input("enter visitor name (or 'exit): ")
    if name == "exit":
        break
    visitors.add(name)

print("total unique visitors:", len(visitors))

# Mini Project 6: String Formatter Tool

name = input("enter name: ")
product = input("enter product: ")

print(f"{name} bought {product}")

print("left:", name.ljust(20))
print("right:", name.rjust(20))
print("center:", name.center(20))

# Mini Project 7: Bank Account System

account = {"name": "dhinesh", "balance": 1000}

while True:
    print("\n1.deposit 2.withdraw 3.check 4.exit")
    choice = input("enter choice: ")

    if choice == "1":
        amount = float(input("enter amount: "))
        account["balance"] += amount
    
    elif choice == "2":
        amount = float(input("enter amount: "))
        if amount <= account["balance"]:
            account["balance"] -= amount
        else:
            print("insufficient balance")
    
    elif choice == "3":
        print("balance:", account["balance"])
    
    elif choice == "4":
       break

                       
# Mini Project 8: Voting System

votes = {"A": 0, "B": 0, "C": 0}

for i in range (5):
    vote = input("vote (A/B/C): ")
    if vote in votes:
        votes[vote] += 1

winner = max(votes, key=votes.get)
print("winner is:", winner)

# Mini Project 9: Course Enrollment System


students = {}
name = input("enter student name: ")
courses = input("enter courses (comma seperated): ").split(",")
students[name] = courses
print("student data:", students)

# Mini Project 10: Number Utility Tool


num = int(input("enter number: "))

print("binary:", bin(num))
print("octal:", oct(num))
print("hex:", hex(num))

print("with commas:", f"{num:,}")
print("scientific:", f"{num:.2e}")
