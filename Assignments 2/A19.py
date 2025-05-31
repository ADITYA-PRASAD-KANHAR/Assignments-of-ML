# 9. Create a function that accepts a list of integers and returns only the even ones.

def even_int(ls):
    ls1 = []
    for i in ls:
        if i%2==0:
            ls1.append(i)

    return ls1

print(even_int([1,2,3,4,5,6,7,8,9]))