def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)



text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))