

def factorial(num):

    if  num==0:

        return 1
    
    return(num*factorial(num-1))

print(factorial(5))

"""
factorial(5)=120
5*factorial(4)=>5*24=120
4*factorial(3)=>4*6=24
3*factorial(2)=>3*2=6
2*factorial(1)=>2*1=2
1*factorial(0)=>1*1=1
factorial(0)= 1
"""
    
