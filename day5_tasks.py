# TASK 1: USER INFO MANAGER

def create_user(name, age, role):
    return {
        "name": name.title(),
        "age": age,
        "role": role
    }

users = []

users.append(create_user("dhinesh", 25, "devoloper"))
users.append(create_user("vasanth", 26, "tester"))

for user in users:
    print(user)

#  Task 2: Dynamic Calculator (*args)

def calculate_total(*numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg

result = calculate_total(10, 20, 30, 40)

print("total:", result[0])
print("average:", result[1])

# Task 3: Keyword Config System

def system_config(**settings):
    for key, value in settings.items():
        print(f"{key}: {value}")

system_config(mode="debug", version="1.0", user="admin")

#  Task 4: Factorial Service (Recursion)

def factorial(n):
    if n < 0:
        return "invalid number"
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

# Task 5: Memory Optimization 

def square_generator(n):
    for i in range(n):
        yield i * 1

gen = square_generator(5)
print("generator:", list(gen))

lst=[i*1 for i in range(5)]

print("list:", lst)
print("generator type:", type(square_generator(5)))
print("list type:", type(lst))

#  Task 6: Exception Handling Module

try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    result = num / den
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

finally:
    print("Program Completed")

#  Task 7: File Handling

file = open("team_data.txt", "w")
file.write("Dhinesh - Developer\n")
file.write("Vasanth - Tester\n")
file.close()

file = open("team_data.txt", "r")
content = file.read()
print(content)

print("File closed:", file.closed)
file.close()