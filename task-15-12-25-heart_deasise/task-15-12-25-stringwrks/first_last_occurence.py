# Write a program to find the first and last occurrence of a character in a string.

word="python programing"

ch="p"

# first=word.index(ch)
# print("first occurence=",first)
# print("last occurance=",word.rindex(ch))
fist=word.find(ch)

second=word.rfind(ch)

if fist==-1:
    print("string is not find")

else:   

    print(fist)
    print(second)