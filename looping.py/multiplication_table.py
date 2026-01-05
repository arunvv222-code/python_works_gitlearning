# multiplication table of a number

"""
1*2=2
2*2=4
3*2=6
"""

i = 1

number = int(input("enter a number "))
while(i<=10):
    print(i,"*",number,"=",i*number)
    i+=1
