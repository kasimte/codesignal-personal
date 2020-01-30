def checkPalindrome(inputString):
    return inputString == inputString[::-1]

inputString = "aabaa"
print(checkPalindrome(inputString))
