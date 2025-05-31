# 13. Create a function to find the sum of digits of a number.

num = int(input("Enter a number : "))

def sum_Digits(num):
    sum = 0
    for i in range(1,100):
        if num >= 1 and i < num:
            sum += num % 10
            num %= 10
        else:
            break
    return sum

        

print(f"Sum Of the digits of a {num} is {sum_Digits(num)}")

