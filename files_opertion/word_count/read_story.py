
file_path="files_opertion\\word_count\\story.txt"

fr_word=open(file_path,"r")

count={}

for line in fr_word:

    line=line.rstrip("\n")

    word=line.split(" ")
    for w in word:
        w=w.rstrip(",")
        w=w.rstrip(".")

        if not w.isalpha():
            continue

        if w in count:

            count[w]+=1

        else:

            count[w]=1

print(count)

vlaue=max(count.values())

max_value=[k for k,v in count.items() if v==vlaue and k.isalpha()]

print(max_value)


