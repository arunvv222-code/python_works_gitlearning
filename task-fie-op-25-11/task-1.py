"""
Task 1:
Create a text file containing a list of numbers (one number per line). 
Write a Python program to read the numbers from the file and create two separate lists:
one list containing odd numbers and another list containing even numbers. 
Finally, display both lists.

"""

file_path="C:\\Users\\arunv\\OneDrive\\Desktop\\dvelopment-journey\\python-works\\task-fie-op-25-11\\numbers-1.txt"

fr=open(file_path,"r")

odd_number=[]
even_number=[]

for line in fr:
    line=int(line.rstrip("\n"))
    
    if line%2==0:
        even_number.append(line)
    else:
        odd_number.append(line)

print(even_number)
print(odd_number)

