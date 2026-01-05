file_path="C:\\Users\\arunv\\OneDrive\\Desktop\\dvelopment-journey\\python-works\\files_opertion\\greetings.txt"

fr=open(file_path,"r")

for line in fr:
    print(line,end="")


st={line.rstrip("\n") for line in fr}

# print(st)
