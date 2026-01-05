
file_path="task-fie-op-25-11\\last_digit.txt"

fr = open(file_path,"r")

for line in fr:
    print(line[-2])