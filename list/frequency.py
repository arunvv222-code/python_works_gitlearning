arr=[100,200,300,110,210,200,100,110,100]

frequent_numbers=[]

for n in arr:
   occ= arr.count(n)

   if occ>1 and n not in frequent_numbers:
      frequent_numbers.append(n)
      continue

print(frequent_numbers)
