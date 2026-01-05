def first_recursive(word):

    wc={}

    for ch in word:
        if ch in wc:

            return(ch)
        else:
            wc[ch]=1

    return None

print(first_recursive("balloon"))