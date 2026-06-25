def bill(units, rate=8):
    return units * rate

units = int(input("Enter units: "))
print("Total Bill = ₹", bill(units))