#  1. Positive Number – Even or Odd

# Task:
# Ask the user to enter a number.
# If the number is positive:
# If even → Print "Positive Even Number"
# Else → Print "Positive Odd Number"
# Else → Print "Not a positive number"


num = int(input("enter a  number "))

if(num>0 and num%2==0):
    print("positive even number")
elif(num>0 and num%2!=0):
    print("postive odd number")
else:
    print("not a positive number")
    