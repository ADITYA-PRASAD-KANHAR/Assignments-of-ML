# 11. Print "Odd" or "Even" for numbers 1 to 10.
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i}: Even")
    else:
        print(f"{i}: Odd")