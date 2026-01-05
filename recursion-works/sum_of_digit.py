

def sum_digit(number):

    if number==0:

        return 0
    return number%10+sum_digit(number//10)

print(sum_digit(123))

   
"""
sum_digit(123)
123%10+123//10=>
12%10+12//10=>
1%10+1//10=>
sum_digit(0)=0

"""
    



