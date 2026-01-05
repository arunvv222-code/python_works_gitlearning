# read a number

# display fizz it divisible by 3

# display buzz it divisible by 5


# dispilay fizzbuzzz it divisible by 15


number = int(input("enter a number"))

if(number%15 == 0):
    print("fizzbuzz")
elif(number%3 == 0):
    print("fizz")
elif(number% 5==0):
    print("buzz")
else:
    print("invalid")

    

