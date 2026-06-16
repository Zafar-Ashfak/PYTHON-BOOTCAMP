# Write a function count_vowels(text) that returns the number of vowels in a string.

# Simple Approach
def count_vowels(text):
    count = 0
    text = text.lower()
    for i in text:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count += 1

    return count


# Optimized Approach
def opt_count_vowels(text):
    count = 0
    text = text.lower()
    for i in text:
        if i in "aeiou":
          count += 1

    return count


user_input = input("Enter a text: ")
# res = count_vowels(user_input)
res = opt_count_vowels(user_input)
print(f"Total number of vowels in the text is: {res}")