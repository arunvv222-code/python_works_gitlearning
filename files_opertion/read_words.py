file_path="C:\\Users\\arunv\\OneDrive\\Desktop\\dvelopment-journey\\python-works\\files_opertion\\words.txt"

fr =open(file_path,"r")

for line in fr:

    line=line.rstrip("\n")

    word=line.replace(" ","")
    
    print(word)