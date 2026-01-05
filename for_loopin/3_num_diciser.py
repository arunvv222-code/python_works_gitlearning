num1=int(input("enter number1 "))
num2=int(input("enter number2 "))
num3=int(input("enter number3 "))

small=min(num1,num2,num3)

for i in range(1,small+1):
    
    if num1%i==0 and num2%i==0 and num3%i==0:

        print(i)