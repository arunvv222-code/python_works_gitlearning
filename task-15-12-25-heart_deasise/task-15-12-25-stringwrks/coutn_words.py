# Write a program to count the number of words in a string using string methods.

words="banana"

count_words={}

for i in words:
    if i in count_words:

        count_words[i]+=1
    else:
        count_words[i]=1

print(count_words)
