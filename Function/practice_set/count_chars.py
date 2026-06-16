# Write a function count_characters(text) that returns the number of characters in a string.

print("Program to count characters of the given text")
def count_characters(text):
   return len(text)

user_input = input("Enter a text: ")
print(f"The total characters in the text is: {count_characters(user_input)}")
