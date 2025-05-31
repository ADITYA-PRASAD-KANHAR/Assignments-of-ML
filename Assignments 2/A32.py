# 32. Write a function to find the most frequent element in a list. 

def most_frequent(lst):
    return max(set(lst), key=lst.count)

print(most_frequent([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]))

