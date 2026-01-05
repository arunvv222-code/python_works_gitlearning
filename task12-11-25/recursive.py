word=["hello","hi","hello","is"]
recursive_word=[]
non_recursive=[]

for w in word:
    if w in non_recursive:
        non_recursive.remove(w)
        recursive_word.append(w)
    elif w not in recursive_word:
        non_recursive.append(w)
print(recursive_word)
print(non_recursive)