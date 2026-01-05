def palindrome(word):
    pal_word=word[::-1]
    return True if pal_word==word else False

print(palindrome("level"))
print(palindrome("cat"))
print(palindrome("madam"))

