


def palindrome(word):
    str1 = word.lower()
    str2 = str1[::-1]
    if(str1 == str2):
        return True
    else:
        return False

print(palindrome("Madam"))
