
file_path="C:\\Users\\arunv\\OneDrive\\Desktop\\dvelopment-journey\\python-works\\task-fie-op-25-11\\last_digit.txt"

fr=open(file_path,"r")

last_dig=[]

for line in fr:
    line=int(line.rstrip("\n"))

    number=line%10

    last_dig.append(number)

print(last_dig)

   