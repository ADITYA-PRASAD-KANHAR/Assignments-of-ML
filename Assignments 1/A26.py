# 26. Find the maximum in a list using loop.

def find_maximum(lst):
    if not lst:
        return None  
    max_val = lst[0]
    for num in lst[1:]:
        if num > max_val:
            max_val = num
    return max_val


numbers = [3, 7, 2, 9, 4]
print("Maximum value:", find_maximum(numbers))