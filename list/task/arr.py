arr=[1,5,7,9,12,15,16,19,20]

even_count=0
odd_count=0

for n in arr:
    if n%2==0:
        even_count+=1
        print(n,"is even")
    elif n%2!=0:
        odd_count+=1
        print(n,"is odd")
print("even couunt=",even_count)
print("odd count=",odd_count)
