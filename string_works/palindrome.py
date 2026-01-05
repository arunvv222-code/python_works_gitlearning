def is_palindrome(word):
    word = word.casefold()
    reversed_word = word[::-1]
    return True if reversed_word == word else False
print(is_palindrome("radar"))


