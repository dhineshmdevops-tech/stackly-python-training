visitors = set()

while True:
    name = input("enter visitor name (or 'exit): ")
    if name == "exit":
        break
    visitors.add(name)

print("total unique visitors:", len(visitors))
