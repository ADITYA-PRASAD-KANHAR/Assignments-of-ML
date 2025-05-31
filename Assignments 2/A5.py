#Create a function to count the number of vowels in a string.
def vowels(n):
    counts = 0
    for i in (n):
        if(i in ['A','E','I','O','U','a','i','o','u','e']):
            counts += 1
    return counts
string = input("enter a string : ")
v = vowels(string)
print(f"In the string {string} , there are {v} number of vowels.")