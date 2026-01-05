s1="python"
s2="typhon"

if len(s1)!=len(s2):

    print("not a anagram")
elif set(s1)==set(s2):
    print("is anagram")
else:
    print("not")
