

def gcd(num1,num2):
    small=min(num1,num2)
    gcd=0
    for i in range(1,small+1):
        if num1%i==0 and num2%i==0:
            gcd = i
        
    return gcd
print(gcd(8,4))