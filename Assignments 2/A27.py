# 27. Create a function that accepts a sentence and returns the longest word. 
def longest_word(sentence):
    words = sentence.split()
    if not words:
        return ""
    return max(words, key=len)

print(longest_word("i am the best person infront of my parents"))

