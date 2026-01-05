"""Task 2:
Create a text file with a list of numbers. 
Write a Python program to read all numbers from the file and create a list of perfect numbers. 
Display only the perfect numbers.

"""


file_path="C:\\Users\\arunv\\OneDrive\\Desktop\\dvelopment-journey\\python-works\\task-fie-op-25-11\\numbers-1.txt"

fr=open(file_path,"r")
perfect_number=[]

for line in fr:
    sum=0
    line=int(line.rstrip("\n"))
    for i in range(1,line):
        if line%i==0:
            sum+=i
    if sum==line:
        perfect_number.append(sum)

print(perfect_number)
