# 15. Write a function that returns the average of a list of numbers

def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print(average(numbers=[9,8,7,6,5,4,3,2]))