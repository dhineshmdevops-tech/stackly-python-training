file = open("team_data.txt", "w")
file.write("Dhinesh - Developer\n")
file.write("Vasanth - Tester\n")
file.close()

file = open("team_data.txt", "r")
content = file.read()
print(content)

print("File closed:", file.closed)
file.close()