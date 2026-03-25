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