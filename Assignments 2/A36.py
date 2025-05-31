# 36. Write a function that returns a list of tuples (element, index) from a list. 

def element_index_tuples(lst):
    return [(element, index) for index, element in enumerate(lst)]

print(element_index_tuples(['a', 'b', 'c']))

