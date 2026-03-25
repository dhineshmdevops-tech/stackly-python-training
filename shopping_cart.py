cart = []

while True:
    print("\n1. add 2.remove 3.show 4.exit")
    choice = input("enter choice: ")

    if choice == "1":
        name = input("product name: ")
        price = float(input("price: "))
        qty = int(input("quantity: "))
        cart.append({"name": name, "price": price, "qty": qty})
        print("item added")

    elif choice == "2":
        name = input("enter product to remove: ")
        for item in cart:
            if item["name"] == name:
                cart.remove(item)
                print("removed")
                break
    elif choice == "3":
        total = 0
        for item in cart:
            price(item)
            total += item["price"] * item["qty"]
        print("total bill:", total)

    elif choice == "4":
        break