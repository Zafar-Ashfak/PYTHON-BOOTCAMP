# Write a program to count the digits in a number using recursion

def countdigits(n):
    count = 0
    # Base Case
    if n == 0:
        return 0
    # Work + Recursion Call
    return 1 + countdigits(n // 10)

def main():
    print("Program to count the digits in a number using recursion")
    n = int(input("Enter a number: "))
    count = countdigits(n)
    print(f"Total number of digits of the number is: {count}")

main()