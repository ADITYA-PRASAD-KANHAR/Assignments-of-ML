# 14. Write a function that takes a string and returns a dictionary of character frequencies.

def char_frequencies(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

print(char_frequencies("banana"))