# Write a program to reverse a string using recursion
def reverse(text, i):
    # Base Case
    if i < 0:
        return ""
    # Recursion Call
    return text[i] + reverse(text, i - 1)

def main():
    print("Program to reverse a string using recursion")
    text = input("Enter a string: ")
    res = reverse(text, len(text) - 1)
    print(res)

main()