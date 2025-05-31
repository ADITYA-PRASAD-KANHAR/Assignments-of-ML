# 37. Create a function that accepts a string and returns a dictionary of word counts. 

def word_count(sentence):
    words = sentence.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

print(word_count("this is a test this is only a test"))

