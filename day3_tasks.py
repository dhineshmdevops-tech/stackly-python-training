# Day 3 - TASKS 
# Section 1: Loop Basics (1–10))

# 1. Print numbers from 1 to 50
for i in range(1,51):
    print (i)

# 2. Even numbers from 1 to 100
for i in range (2, 101, 2):
    print(i)

# 3. Odd numbers
for i in range(1, 101, 2):
    print(i)

# 4. Table of 7
for i in range(1, 11):
    print(f"7 x {i}={7*i}")
# 5. Sum 1 to 100
total = 0
for i in range (1, 101):
    total += i
    print(total)

# 6. Reverse 50 to 1
for i in range(50, 0, -1):
    print(i)

# 7. Count divisible by 3
count = 0
for i in range(1, 101):
    if i %3 == 0:
        count +=1
print(count)
# 8. Squares 1 to 10
for i in range ( 1, 11):
    print(i*i)

# 9. Cubes 1 to 10
for i in range(1, 11):
    print(i**3)

# 10. Input n
n= int(input("Enter number: "))
for i in range(1,n+1):
    print(i)

# SECTION 2: While Loop

# 11. 1 to 20
i=1
while i<=20:
    print(i)
    i += 1

# 12. Factorial
n=int(input("Enter number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)

# 13. Reverse number
num = int(input("Enter number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev* 10 + digit
    num //= 10
print(rev)

# 14. Count digits
num = int(input("Enter number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print(count)

# 15. Until "stop"
while True:
    data = input("Enter something: ")
    if data.lower() == "stop":
        break
# SECTION 3: Nested Loop

# 16. *
for i in range(1, 5):
    print("*" * i)

# 17. Number pattern
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end="")
    print()

# 18. Table 1 to 5
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i}x{j}={i*j}", end=" ")
    print()

# 19. A B C
for i in range(3):
    print("A B C")

# 20. 1 to 9 matrix
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()

# SECTION 4: String Basics

# 21. Count characters
s = input("Enter string: ")
print(len(s))

# 22. Count vowels
count = 0
for ch in s.lower():
    if ch in "aeiou":
        count += 1
print(count)

# 23. Count consonants
count = 0
for ch in s.lower():
    if ch.isalpha() and ch not in "aeiou":
        count += 1
print(count)

# 24. Reverse string
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

# 25. Palindrome
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#SECTION 5: String Slicing

#  26. first 5
s = "DevOpsEngineer"
print(s[:5]) 

# 27. last 3
s = "DevOpsEngineer"
print(s[-3:]) 

# 28. reverse
s = "DevOpsEngineer"
print(s[::-1])  

# 29. every 2nd
s = "DevOpsEngineer"
print(s[::2])   

# 30. remove first & last
s = "DevOpsEngineer"
print(s[1:-1])    

# SECTION 6: List Basics
# 31. Sum
lst = [10, 20, 30, 40, 50]
total = sum(lst)
print(total)

# 32. max
lst = [10, 20, 30, 40, 50]
print(max(lst))

# 33. Min
lst = [10, 20, 30, 40, 50]
print(min(lst))

# 34. Len
lst = [10, 20, 30, 40, 50]
print(len(lst))

# 35. Exist
lst = [10, 20, 30, 40, 50]
x = 30
if x in lst:
    print("Exists")
else:
    print("Not Found")

# SECTION 7: List Operations
# 36.  append 
lst = [1, 2, 3]

lst.append(4)
lst.append(5)
lst.append(6)

print(lst)

# 37. insert
lst = [10, 20, 30]

lst.insert(1, 99)

print(lst)

# 38. remove
lst = [1, 2, 3, 4]

lst.remove(3)

print(lst)

# 39. reverse without reverse()
lst = [1, 2, 3, 4]

rev = []

for i in lst:
    rev = [i] + rev

print(rev)

# 40. sort without sort()
lst = [5, 2, 8, 1]

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print(lst)