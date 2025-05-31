# 17. Print ASCII values of characters in a string.

input_str = input("Enter a string: ")

for char in input_str:
    print(f"'{char}': {ord(char)}")