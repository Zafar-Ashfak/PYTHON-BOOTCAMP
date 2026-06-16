# Write a function reverse_string(text) that returns the reversed string.

# Reverse the given string using a variable
def reverse_string(text):
    rev = ""
    for char in text:
        rev = char + rev

    return rev

user_input = input("Enter a text: ")
print(reverse_string(user_input))


# Reverse the given string using slicing notation
def reverse_string(text):
    return text[::-1]

user_input = input("Enter a string: ")
print(reverse_string(user_input))