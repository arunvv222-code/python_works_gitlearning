word="abcdcdbaabcd"
     #012345678901
count=0
search_word="cd"
for i in range(0,11):
    s_word=word[i:i+2]

    if search_word==s_word:
        count+=1
print(count)


    

