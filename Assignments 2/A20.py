# 20. Write a function to check if all characters in a string are unique. 

def check_string(str):
    inc = 0
    for i in str:
        inc += 1
        if i in str[inc:]:
            return False
    else:
        return True

print("no repeatation" if check_string("hello") == True else "here is a repeatation" )


 
 





