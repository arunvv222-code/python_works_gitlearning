# words=["hai","hello","hai","hello","python"]
# count_w={}
# for w in set(words):
#     count_w[w]=words.count(w)
# print(count_w)

words=["hai","hello","hai","hello","python"]

wc={}

for w in words:

    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1
print(wc)


