# print numbers from 1 to 50 divisible by both 2 and 3

num = 1

while num<=50:
    if num%2==0 and num%3==0:
        print(num,"is divisible by both 2 and 3")

    num+=1