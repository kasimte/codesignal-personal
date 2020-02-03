def checkPalindrome(inputString):
    return inputString == inputString[::-1]

print(checkPalindrome("aabaa")) # True
print(checkPalindrome("010110")) # False
print(checkPalindrome("ab3ba")) # True
