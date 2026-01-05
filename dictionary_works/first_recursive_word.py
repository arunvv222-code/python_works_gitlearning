word="balloon"

wc={}

for w in word:
    if w not in wc:
        wc[w]=1
    else:
        print(w)
        break