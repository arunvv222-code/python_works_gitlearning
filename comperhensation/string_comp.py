word=["profession","cat","act","program","dam","process"]
#w.a.p to create a new list thats contain words start with "pro"

st=[w for w in word if w.startswith("pro")]
print(st)

#w.a.p to create a new list thats contain words ends with "am"

ends_word={w for w in word if w.endswith("am")}

print(ends_word)