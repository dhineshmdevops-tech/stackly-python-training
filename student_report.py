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
