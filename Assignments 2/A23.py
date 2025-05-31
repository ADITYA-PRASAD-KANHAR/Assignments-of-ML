# 23. Create a function to remove duplicates from a list. 
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

print(remove_duplicates("Hello world"))

