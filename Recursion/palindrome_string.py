#  Write a program to check if a string is a palindrome using recursion
def palindrome(text, lp, rp):
    # Base Case
    if lp >= rp:
        return True

    elif text[lp] != text[rp]:
        return False

    return palindrome(text, lp = lp +1, rp = rp - 1)

def main():
    print("Program to check if a string is a palindrome")
    text = input("Enter a string: ")
    if palindrome(text, 0, len(text) - 1):
        print(f"'{text}' is a palindrome string")
    else:
        print(f"'{text}' is not a palindrome string")


main()