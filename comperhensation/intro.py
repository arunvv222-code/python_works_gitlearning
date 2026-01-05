arr=[2,3,4,5,6,8,9,10]

squares=[ num**2 for num in arr]

even=[num for num in arr if num%2==0]

odd =[num for num in arr if num%2!=0]

num_gt_five=[num for num in arr if num>5]

print(num_gt_five)
print(even)
print(odd)
print(squares)