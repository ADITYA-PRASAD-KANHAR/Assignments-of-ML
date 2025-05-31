# 7. Create a function to calculate the sum of a list of numbers.

def list_Add(list):
    sum = 0
    for i in list:
        sum += i
    return sum

ls = [1,2,3,4,5,6,7,8,9]
print(list_Add(ls))