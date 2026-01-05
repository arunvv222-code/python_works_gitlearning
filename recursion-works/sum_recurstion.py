

def sum(limit):

    if limit==1:

        return 1
    return limit+sum(limit-1)

print(sum(5))

"""
sum(5)=15
5+sum(4)=>5+10=15
4+sum(3)=>4+6=10
3+sum(2)=>3+3=6
2+sum(1)=>2+1=3

sum(1)=1

"""

   

