# 6. Write a function to check if a string is a palindrome.

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


print(is_palindrome("Madam"))  
print(is_palindrome("Hello"))  