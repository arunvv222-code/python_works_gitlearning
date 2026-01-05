file_name="task-fie-op-25-11\\names.txt"

fr=open(file_name,"r")

for line in fr:

    line=line.rstrip("\n")
    first_ch=line[0]
    last_ch=line[-1]

    print(first_ch,"-",last_ch)
    