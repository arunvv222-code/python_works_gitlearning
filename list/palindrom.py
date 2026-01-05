def palindrom(words):
    p_word=[]
    for w in words:
        if w==w[::-1]:
            p_word.append(w)
    return p_word

words=["cat","act","dam","mad","malayalam","madam"]
print(palindrom(words))
    


