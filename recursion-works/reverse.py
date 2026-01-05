
def reverse(num):

    if num==0:

        return ""
    
    return str(num%10) + str(reverse(num//10))

print(reverse(123))