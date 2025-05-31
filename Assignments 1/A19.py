# 19. Check if a number is divisible by 2 or 3.

num = int(input("Enter a number: "))

if num % 2 == 0 or num % 3 == 0:
    print(f"{num} is divisible by 2 or 3.")
else:
    print(f"{num} is not divisible by 2 or 3.")