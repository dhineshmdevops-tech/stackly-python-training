# Day 2 Tasks List

# Task 1- 8 (Bitwise Operators)
# 1
a = 10
b = 6
print(a & b)

# 2
x = 12
y = 5
print(x | y)

# 3
num = 8
print(~num)

# 4
a = 15
b = 9
print(a ^ b)

# 5
num = 7
print(num << 2)

# 6
num = 20
print(num >> 1)

# 7
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("AND result:", a & b)

# 8
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("XOR result:", a ^ b)

# Task 9-14 Strings
# 9
s = "hi"
print(s * 4)

# 10
s = "python"
print(s * 3)

# 11
a = "super"
b = "man"
print(a + b)

# 12
a = "hello"
b = " "
c = "world"
print(a + b + c)

# 13
name = input("Enter your name: ")
print(name * 5)

# 14
a = input("Enter first string: ")
b = input("Enter second string: ")
print(a + b)

# Tasks 15- 20 ( Input & Type Casting)
# 15
name = input("Enter your name: ")
print(type(name))

# 16
age = int(input("Enter age: "))
print(age)

# 17
a = int(input("Enter number: "))
b = int(input("Enter number: "))
print("Sum:", a + b)

# 18
m1 = float(input("Enter mark1: "))
m2 = float(input("Enter mark2: "))
print("Average:", (m1 + m2) / 2)

# 19
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(3*a*2 + b - 2)

# 20
num = input("Enter number: ")
print("Before:", type(num))
num = int(num)
print("After:", type(num))

# Tasks 21–25 (Digits)
# 21
num = input("Enter number: ")
print("Last digit:", num[-1])

# 22
num = int(input("Enter number: "))
print(num % 10)

# 23
num = int(input("Enter number: "))
print(num // 10)

# 24
num = int(input("Enter number: "))
print((num // 10) % 10)

# 25
num = int(input("Enter 5 digit number: "))
print(num % 10)

# Tasks 26–30 (If)

# 26
if 10 >= 5:
    print("10 is greater than or equal to 5")

# 27
num = int(input("Enter number: "))
if num > 50:
    print("Number is greater than 50")

# 28
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible")

# 29
num = int(input("Enter number: "))
if num > 100:
    print("Greater than 100")

# 30
num = int(input("Enter number: "))
if num >= 0:
    print("Non negative number")

# Tasks 31–34 (If-Else)
# 31
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 32
marks = int(input("Enter marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Fail")

# 33
num = int(input("Enter number: "))
if num >= 0:
    print("Positive")
else:
    print("Negative")

# 34
num = int(input("Enter number: "))
if num > 10:
    print("Greater than 10")
else:
    print("Not greater than 10")

# Tasks 35–37 (Nested If)
# 35
age = int(input("Age: "))
height = int(input("Height: "))
weight = int(input("Weight: "))

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")


# 36
marks = int(input("Marks: "))
age = int(input("Age: "))

if marks >= 60:
    if age >= 17:
        print("Admission Granted")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")


# 37
age = int(input("Age: "))
height = int(input("Height: "))
weight = int(input("Weight: "))

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")

# Tasks 38–40 (Match Statement)
# 38
day = int(input("Enter number 1-7: "))

match day:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")


# 39
color = int(input("Enter number 1-3: "))

match color:
    case 1: print("Red")
    case 2: print("Blue")
    case 3: print("Green")


# 40
fruit = int(input("Enter number 1-4: "))

match fruit:
    case 1: print("Apple")
    case 2: print("Mango")
    case 3: print("Orange")
    case 4: print("Banana")