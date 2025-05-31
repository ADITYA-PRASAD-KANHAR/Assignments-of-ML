# 28. Write a function to compute the power of a number using recursion.

def recursive_power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / recursive_power(base, -exponent)
    else:
        return base * recursive_power(base, exponent - 1)


print(recursive_power(2, 3))   
print(recursive_power(5, 0))   
print(recursive_power(2, -2))  

