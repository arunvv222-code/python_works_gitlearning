lst=[3,6,9,12,14,2]


evens=list(filter(lambda x: x%2==0,lst))

print(evens)

odd=list(filter(lambda x: x%2!=0,lst))

print(odd)