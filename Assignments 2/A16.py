# 16. Create a function that accepts a number and prints its multiplication table.

def print_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

print(print_multiplication_table(49))