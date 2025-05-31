#Create a function to find the maximum of three numbers.
def max_Three(a,b,c):
    if (a >= b and a >= c):
        return a
    elif (b>= c and b >= a):
        return b
    else:
        return c
print(max_Three(1200,300,340))