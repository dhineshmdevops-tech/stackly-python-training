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