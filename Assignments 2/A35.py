# 35. Write a function that accepts variable number of arguments and returns their product. 

def product(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(product(2, 3, 4))
print(product(5, 10))
print(product(7))

