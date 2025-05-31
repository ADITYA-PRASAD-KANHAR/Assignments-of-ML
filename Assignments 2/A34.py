# 34. Create a function that finds the intersection of two lists. 

def intersection(list1, list2):
    return list(set(list1) & set(list2))

print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))


