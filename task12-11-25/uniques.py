num=[1,2,2,3,4,4,5]

unique_word=set()

for n in num:
    if num.count(n)==1:
        unique_word.add(n)
print(unique_word)