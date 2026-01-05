file_path="Eror_handling\\number.txt"
fr=open(file_path,"r")
number_list=[]

for line in fr:
    line.rstrip("\n")

    try:
        number=int(line)
        number_list.append(number)
    except Exception as e:
        continue

even_numbers=[num for num in number_list if num%2==0]

count_even_num={n:number_list.count(n) for n in even_numbers}

print("even number:",even_numbers)
print("count even:",count_even_num)

max_cout=[k for k,v in count_even_num.items() if v==max(count_even_num.values())]




    



