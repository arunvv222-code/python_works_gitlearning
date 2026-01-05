def pangram(word):
    alphabet ="abcdefghijklmnopqrstuvwxyz"

    is_pangram=True

    for al in alphabet:
        if al not in word.casefold():
             is_pangram=False

             break
    return is_pangram

print(pangram("THE QUICK BROWN FOX JUMPS OVER LAZY DOG"))
print(pangram("he is lazy boy"))