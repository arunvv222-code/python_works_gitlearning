file_path="C:\\Users\\arunv\\OneDrive\\Desktop\\dvelopment-journey\\python-works\\files_opertion\\words.txt"

fr = open(file_path,"r")

result=[]

for line in fr:

    line=line.rstrip("\n")

    word=line.replace(" ","")

    if word==word[::-1]:
        result.append(word)

print(result)

