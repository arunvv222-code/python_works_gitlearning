file_path="C:\\Users\\arunv\\OneDrive\\Desktop\\dvelopment-journey\\python-works\\files_opertion\\numbers.txt"

fr = open(file_path,"r")

result=[]

for line in fr:

    number=line.rstrip("\n")

    rev=number[::-1]

    result.append(rev)

print(result)






    

    