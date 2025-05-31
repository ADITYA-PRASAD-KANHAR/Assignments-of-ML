# 39. Count uppercase and lowercase letters in a string.
def count_upper_lower(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower


text = "Hello World!"
upper_count, lower_count = count_upper_lower(text)
print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")