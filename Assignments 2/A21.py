# 21. Create a function to calculate the greatest common divisor (GCD) of two numbers. 

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(2,3))

