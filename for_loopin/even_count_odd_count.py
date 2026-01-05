num = int(input("enter a number "))
even=0
odd = 0
for i in range(1,num+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print(odd)
print(even)
