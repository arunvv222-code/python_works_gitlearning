num = int(input("enter a number ")) #123

while num!=0: #123!=0
    
    last_digit = num%10 #123%10=3
    sqr = last_digit**2 #3**2=9
    print(sqr)

    num = num//10