"""
Erorhandling
1.syntax error
2.logical error
3.runtime error(exception)zerodivision error ,filenotfound,key error,value error

block of error handling
try:
except:
finally:

keywords used

raise
assert

syntax

try:
    doubtful codes
except:
    handling code
finally:
    cleanup process

"""
num1=int(input("enter a number "))

num2=int(input("enter num2 "))

try:
    div=num1/num2

    print(div)
except Exception as e:
    print(e)

print("file is good")
print("krishna is god")