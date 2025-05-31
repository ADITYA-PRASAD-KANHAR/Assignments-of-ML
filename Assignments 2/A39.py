# 39. Create a function that accepts a list and a value, and returns the index of the value (or -1). 

def find_index(lst, value):
    try:
        return lst.index(value)
    except ValueError:
        return -1

print(find_index([1, 2, 3, 4, 5], 3))
print(find_index([1, 2, 3, 4, 5], 6))

