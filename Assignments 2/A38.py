# 38. Write a function that checks if a sentence is a pangram. 

def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(sentence.lower())

print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello world"))

