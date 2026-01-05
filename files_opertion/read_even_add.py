file_path="C:\\Users\\arunv\\OneDrive\\Desktop\\dvelopment-journey\\python-works\\files_opertion\\numbers.txt"

fr = open(file_path,"r")

odd_number=[]

even_number=[]

for line in fr:

    number=int (line.rstrip("\n"))

    if number%2==0:
        even_number.append(number)
    else:
        odd_number.append(number)

print(odd_number)
print(even_number)
    
    
