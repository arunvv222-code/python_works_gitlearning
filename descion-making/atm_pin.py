db_pin = 2468
db_balance = 5000

pin = int(input("enter the pin number"))

if db_pin == pin:
    amount = int(input("enter amount "))
    if amount <= db_balance:
        print("trancation is success")
    else:
        print("insufficient balance")
else:
    print("incorrect pin")


