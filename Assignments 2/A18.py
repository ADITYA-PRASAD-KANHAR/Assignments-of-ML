# 18. Write a function to find the second largest number in a list.
def second_largest(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

print(second_largest([7,3,9,1,2,8,6,4,5,0]))