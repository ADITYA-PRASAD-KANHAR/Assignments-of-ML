# 12. Write a function to check if a number is a perfect number.

def is_Perfect(number):
    sum = 0
    for i in range(1,number):
        if number % i == 0:
            sum += i
    return " is a perfect number." if sum == number else "is not a perfect number."

number = int(input("Enter a number : "))


print(f"The number {number} {is_Perfect(number)}")