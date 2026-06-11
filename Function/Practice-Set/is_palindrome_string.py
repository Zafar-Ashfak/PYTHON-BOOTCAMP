# Write a function to check if a string is palindrome or not

def is_palindrome_string(text):
    lp = 0
    rp = len(text) - 1

    while lp <= rp:
        if text[lp] != text[rp]:
            return False

        elif text[lp] == text[rp]:
            lp += 1
            rp -= 1

    return True

def main():
    print("Program to check if a string is palindrome or not")
    text = input("Enter a string: ")
    if is_palindrome_string(text):
        print(f"{text} is a palindrome string")
    else:
        print(f"{text} is not a palindrome string")

main()