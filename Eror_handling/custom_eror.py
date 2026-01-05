# age = int(input("enter age"))

# if age<18:
#     raise Exception("invalid age")
# else:
#     print("eligible for vote")

age=int(input("enter a age"))

if age<0:
    raise Exception ("invalid age")
else:
    print("valid")