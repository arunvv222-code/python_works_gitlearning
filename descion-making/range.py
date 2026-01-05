number = int(input("enter a number "))

if number in range(1,6):
    print("weekday")
elif number in range(6,8):
    print("weekend")
else:
    print("invalid")

