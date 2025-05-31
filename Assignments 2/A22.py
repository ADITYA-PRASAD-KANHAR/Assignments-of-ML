# 22. Write a function to find the least common multiple (LCM) of two numbers. 
def lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b) if a and b else 0

print(lcm(2,3))

