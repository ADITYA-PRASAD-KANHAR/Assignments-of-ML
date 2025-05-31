# 33. Create a function that returns the median of a list. 

def median(lst):
    lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2
    else:
        return lst[mid]

print(median([1, 3, 2, 4, 5]))
print(median([1, 2, 3, 4]))

