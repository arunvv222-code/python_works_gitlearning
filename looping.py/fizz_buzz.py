"""
fizz buzz from 1 to 20

fiz divisble by 3
buzz divisible by 5
fizz buzz div by both
else print number
"""

number = 1

while (  number <= 20): #6

    if number%3==0 and number %5==0:
        print("fizz buzz")
    elif number%3==0:
            print("fizz ")
    elif  number%5==0:
            print("buzz")

    else:
        print(number)

    number+=1