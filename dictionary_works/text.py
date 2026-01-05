text="hello world"

wc={}

for w in text:
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1
print(wc)