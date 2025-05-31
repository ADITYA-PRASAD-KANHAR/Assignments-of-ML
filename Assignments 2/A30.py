# 30. Write a function to check if a list is sorted. 
def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

print(is_sorted([1, 2, 3, 4, 5]))    
print(is_sorted([5, 3, 2, 1]))       

