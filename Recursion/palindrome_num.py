# Write a program to check if a number is a palindrome using recursion

# Helper function
def reverse(num, rev):
    # Base Case
    if num == 0:
        return rev

    rem = num % 10
    rev = rev * 10 + rem
    return reverse(num // 10, rev)

def palindrome(num):
    return num == reverse(num, 0)

def main():
    print("Program to check if a number is a palindrome")
    num = int(input("Enter a natural number: "))

    if palindrome(num):
        print(f"{num} is a palindrome number")

    else:
        print(f"{num} is not a palindrome number")

main()