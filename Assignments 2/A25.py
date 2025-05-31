# 25. Create a function that checks if a number is an Armstrong number. 

def is_armstrong(number):
    num_str = str(number)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return total == number

print(is_armstrong(154))

