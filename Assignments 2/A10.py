# 10. Write a function to find the minimum value in a list.

def minimum_value(list):
    small = 1000000
    for i in list:
        if(i < small):
            small = i
    return small

ls = [2,6,2,3,4,8,1,3,5,7,2,4,5,8,1,3]
print(f"In List {ls} the smallest value is : {minimum_value(ls)}")
