account = {
    "Name": "Siddhi",
    "Account Number": "1234567890123",
    "Balance": 10000000,
    "PIN": "1516"
}

if input("Enter PIN: ") == account["PIN"]:

    while True:
        print("\n1.Balance\n2.Withdraw\n3.Deposit\n4.Change PIN\n5.Details\n6.Exit")
        ch = int(input("Enter Choice: "))

        if ch == 1:
            print("Balance:", account["Balance"])

        elif ch == 2:
            amt = int(input("Amount: "))
            account["Balance"] -= amt
            print("Balance:", account["Balance"])

        elif ch == 3:
            amt = int(input("Amount: "))
            account["Balance"] += amt
            print("Balance:", account["Balance"])

        elif ch == 4:
            account["PIN"] = input("New PIN: ")
            print("PIN Changed")

        elif ch == 5:
            print(account["Name"])
            print(account["Account Number"])
            print(account["Balance"])

        elif ch == 6:
            print("Thank You")
            break

else:
    print("Invalid PIN")