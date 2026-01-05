


def vowel_and_c_count(word):
    vowel_count=0
    c_ccount= 0
    VOWELS="aeiou"
    for ch in word:
        if ch in VOWELS:
            vowel_count +=1
        else:
            c_ccount +=1
    print("vowel count=",vowel_count)
    print("consanat count=",c_ccount)
word=input("enter a word ")
vowel_and_c_count(word)

    