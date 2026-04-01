
# TASK 1: ENCAPSULATION

class User:
    def __init__(self):
        self.__user_name = None
        self.__pwd = None

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name

    def register(self):
        print("Registering user:", self.__user_name)

    def login(self):
        print("Logging in:", self.__user_name)


print("\n--- Task 1 Output ---")
u = User()
u.set_user("john", "1234")
u.register()
u.login()



# TASK 2: INHERITANCE

class UserBase:
    def register(self):
        print("User Registered")

    def login(self):
        print("User Logged In")


class Student(UserBase):
    def student_greet(self):
        print("Hello Student")


class Faculty(UserBase):
    def faculty_greet(self):
        print("Hello Faculty")


class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


print("\n--- Task 2 Output ---")
s = Student()
s.register()
s.login()
s.student_greet()

f = Faculty()
f.register()
f.faculty_greet()

tf = TempFaculty()
tf.login()
tf.faculty_greet()
tf.tempFaculty_greet()



# TASK 3: METHOD OVERRIDING


class UserOverride:
    def greet(self):
        print("Welcome User")


class StudentOverride(UserOverride):
    def greet(self):
        print("Welcome Student")


class FacultyOverride(UserOverride):
    def greet(self):
        print("Welcome Faculty")


print("\n--- Task 3 Output ---")
s = StudentOverride()
s.greet()

f = FacultyOverride()
f.greet()



# TASK 4: METHOD CHAINING


class UserChain:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self


print("\n--- Task 4 Output ---")
user = UserChain()
user.login().greet().register()


# TASK 5: COMBINED REAL-TIME

class UserSystem:
    users_count = 0

    def __init__(self, name, pwd):
        self.__name = name
        self.__pwd = pwd
        UserSystem.users_count += 1

    def register(self):
        print("registered:", self.__name)
        return self

    def login(self):
        print("logined:", self.__name)
        return self

    def greet(self):
        print("Welcome User")
        return self


class StudentSystem(UserSystem):
    def greet(self):
        print("Welcome Student")
        return self


class FacultySystem(UserSystem):
    def greet(self):
        print("Welcome Faculty")
        return self


print("\n--- Task 5 Output ---")
u1 = StudentSystem("dhinesh", "111")
u1.login().greet().register()

u2 = FacultySystem("kumar", "222")
u2.login().greet().register()

print("Total Users:", UserSystem.users_count)