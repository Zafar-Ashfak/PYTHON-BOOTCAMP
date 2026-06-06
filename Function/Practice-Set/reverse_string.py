# Write a function reverse_string(text) that returns the reversed string.
def reverse_string(text):
    rev = ""
    for char in text:
        rev = char + rev

    return rev

user_input = input("Enter a text: ")
print(reverse_string(user_input))