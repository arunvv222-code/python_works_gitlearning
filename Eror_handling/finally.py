num1=int(input("enter a number "))
num2=int(input("enter a number2 "))

try:
    result=num1/num2
    print(result)

except Exception as e:
    numn2=int(input("enter a number"))
    
    result=num1/num2
    print(result)

finally:
    print("sending a text message......")
    print("sending email.....")