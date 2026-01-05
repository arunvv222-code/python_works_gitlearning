lst=["10","20","hello","300","hai","4 00"]

# error handling
# sum , min , max , sort

int_list=[]

for n in lst:
    try:
        num=int(n)

        int_list.append(num)
    except Exception as e:
        continue
        
print(int_list)
print(max(int_list))
print(min(int_list))

sorted_el=sorted(int_list)
print(sorted_el)

total=sum(int_list)
print(total)
