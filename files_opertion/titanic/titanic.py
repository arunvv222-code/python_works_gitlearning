file_path="files_opertion\\titanic\\data_set.csv"

fr=open(file_path,"r")

row=fr.readline()

print(row)

for line in fr:
    lst=line.strip("\n").split(",")
    id=lst[0]
    survived=lst[1]
    pclass=lst[2]
    name=lst[3].lstrip('"')
    gendr=lst[5]
    age=lst[6]
    sibsp=lst[7]
    parch=lst[8]
    fare=lst[10]
    cabin=lst[11]
    embraked=lst[12]

    print(name,age,gendr)
