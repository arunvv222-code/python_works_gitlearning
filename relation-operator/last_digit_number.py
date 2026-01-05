"""
check last digit of a number is greater than 5

"""

number = int(input("enter num "))

last_digit = number%10

print(last_digit%2==0)

print(last_digit>5)