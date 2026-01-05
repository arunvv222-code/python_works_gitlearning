

def product(number):

    if number == 1:

        return 1
    
    return number%10*product(number//10)

print(product(123))



