# 30. Count frequency of digits in a number.

def count_digit_frequency(number):
    freq = [0] * 10  # List to store frequency of digits 0-9
    for digit in str(abs(number)):
        if digit.isdigit():
            freq[int(digit)] += 1
    return freq


num = int(input("Enter a number: "))
frequency = count_digit_frequency(num)
for i, count in enumerate(frequency):
    if count > 0:
        print(f"Digit {i}: {count} time(s)")