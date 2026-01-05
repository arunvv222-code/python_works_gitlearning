# lst=[2,3,4,5]

# #   1
    
# for index,num in enumerate(lst,1):

#     print(index + num)

arr=[12,22,23,34]

result={num:num**index for index,num in enumerate(arr)}

print(result)
