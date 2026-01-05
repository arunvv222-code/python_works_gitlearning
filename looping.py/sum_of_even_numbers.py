"""
sum of only even numbers from 1 - 100


"""

num = 1
total = 0

while num<=100:
    if num%2==0:
        total+=num

    num+=1

print("sum of even numbers is ",total)