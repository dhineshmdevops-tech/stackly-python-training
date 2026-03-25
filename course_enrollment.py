students = {}
name = input("enter student name: ")
courses = input("enter courses (comma seperated): ").split(",")
students[name] = courses
print("student data:", students)