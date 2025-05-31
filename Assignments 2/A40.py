# 40. Write a function that counts the number of uppercase and lowercase characters in a string.

def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return {'uppercase': upper, 'lowercase': lower}

print(count_case("Hello World!"))
print(count_case("PYTHON programming"))