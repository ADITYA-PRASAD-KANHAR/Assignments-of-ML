# 11. Create a function to count how many times a character appears in a string.

def character_Counter(sentence,find):
    count = 0
    for i in sentence:
        if find in i:
            count += 1
    return count

sentence = input("Enter full sentence : ")
find = input(f"Enter the element you want to search in \"{sentence}\" : ")

print(f"In sentence {sentence} the character {find} appears {character_Counter(sentence,find)} times.")
