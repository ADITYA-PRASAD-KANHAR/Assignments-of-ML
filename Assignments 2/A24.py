# 24. Write a recursive function to compute the factorial of a number. 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

