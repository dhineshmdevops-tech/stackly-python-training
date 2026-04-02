
# IMPORTS

from abc import ABC, abstractmethod
from functools import reduce



# TASK 1 & 2: SUPER() + ABSTRACTION

class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = int(fees)

    def get_details(self):
        return f"Student: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = int(salary)

    def get_details(self):
        return f"Faculty: {self.name}, ID: {self.id}, Salary: {self.salary}"


class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"


# DATA CREATION

students = [
    Student("dhinesh", 1, "CSE", 60000),
    Student("vasanth", 2, "ECE", 45000),
    Student("arun", 3, "IT", 70000)
]

faculty = [
    Faculty("tamil", 101, 40000),
    Faculty("sita", 102, 25000),
    TempFaculty("magesh", 103, 30000, "6 months")
]


# TASK 3: SORTING

students.sort(key=lambda s: s.fees)
faculty.sort(key=lambda f: f.salary)

print("\n--- Sorted Students (by fees) ---")
for s in students:
    print(s.get_details())

print("\n--- Sorted Faculty (by salary) ---")
for f in faculty:
    print(f.get_details())



# TASK 4: MAP()

student_names = list(map(lambda s: s.name, students))
print("\nStudent Names:", student_names)



# TASK 5: FILTER()

high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

print("\n--- High Fee Students ---")
for s in high_fee_students:
    print(s.get_details())

print("\n--- High Salary Faculty ---")
for f in high_salary_faculty:
    print(f.get_details())



# TASK 6: REDUCE()

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("\nTotal Fees Collected:", total_fees)
print("Total Salary Paid:", total_salary)



# TASK 7: HIGHER ORDER FUNCTION

def process_users(users, func):
    return list(map(func, users))


names_using_hof = process_users(students, lambda s: s.name)
print("\nNames using Higher Order Function:", names_using_hof)



# FINAL MINI SYSTEM 

print("\n========== FINAL SYSTEM OUTPUT ==========")

# All details
print("\nAll Users:")
for s in students:
    print(s.get_details())

for f in faculty:
    print(f.get_details())

# Filter + Map combined
filtered_names = list(map(lambda s: s.name,
                    filter(lambda s: s.fees > 50000, students)))

print("\nFiltered Student Names (fees > 50000):", filtered_names)

# Reduce summary
print("\nSummary:")
print("Total Fees:", total_fees)
print("Total Salary:", total_salary)