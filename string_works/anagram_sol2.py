def is_anagranm(word1,word2):
    is_anagram_word = True

    if len(word1)!=len(word2):
        return False
    for ch in word1:

        ch_word1_count = word1.count(ch)
        ch_word2_count = word2.count(ch)

        if ch_word1_count != ch_word2_count:

            is_anagram_word=False
            break
    return is_anagram_word
print(is_anagranm("cat","act"))
print(is_anagranm("listen","silent"))
