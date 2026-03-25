account = {"name": "dhinesh", "balance": 1000}

while True:
    print("\n1.deposit 2.withdraw 3.check 4.exit")
    choice = input("enter choice: ")

    if choice == "1":
        amount = float(input("enter amount: "))
        account["balance"] += amount
    
    elif choice == "2":
        amount = float(input("enter amount: "))
        if amount <= account["balance"]:
            account["balance"] -= amount
        else:
            print("insufficient balance")
    
    elif choice == "3":
        print("balance:", account["balance"])
    
    elif choice == "4":
       break

                       