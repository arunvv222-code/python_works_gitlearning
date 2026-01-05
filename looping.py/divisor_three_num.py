num1 = int(input("enter num1 "))
num2 = int(input("enter num2 "))
num3 = int(input("enter num3 "))

i=1

small = 0

if num1<num2:
    small=num1
elif num2<num3:
    small=num2
else:
    small = num3

print("small=",small)

while i<=small:

    if(num1%i==0 and num2%i==0 and num3%i==0):

        print(i)
    
    i+=1