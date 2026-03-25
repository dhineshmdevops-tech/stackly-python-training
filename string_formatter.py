name = input("enter name: ")
product = input("enter product: ")

print(f"{name} bought {product}")

print("left:", name.ljust(20))
print("right:", name.rjust(20))
print("center:", name.center(20))
