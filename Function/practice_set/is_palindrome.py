# Write a function palindrome(n) that checks if a number is a palindrome or not.

def palindrome(n):
    org = n
    rev = 0
    while n > 0:
        rem = n % 10
        rev = rev *10 + rem
        n //= 10

    return org == rev

def main():
    num = int(input("Enter a number: "))
    if palindrome(num):
        print(f"{num} is a palindrome number")
    else:
        print(f"{num} is not a palindrome number")


main()

