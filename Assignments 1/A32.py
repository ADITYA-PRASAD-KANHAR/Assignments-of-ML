# 32. Check if a number is a palindrome.

def is_palindrome_number(n):
    return str(n) == str(n)[::-1]


num = int(input("Enter a number: "))
if is_palindrome_number(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")