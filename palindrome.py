#Palindrome checker
def is_palindrome(string):
    if string == string[::-1]:
        return "is palindrome"
    else:
        return "is not palindrome"
print(is_palindrome("madame"))
