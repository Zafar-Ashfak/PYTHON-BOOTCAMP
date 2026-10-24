# Write a program to count the digits in a number using recursion

def count_digits(n : int) -> int:
    count = 0
    # Base Case
    if n == 0:
        return 0
    # Work + Recursion Call
    return 1 + count_digits(n // 10)

def main():
    print("Program to count the digits in a number using recursion")
    n = int(input("Enter a number: "))
    count = count_digits(n)
    print(f"Total number of digits of the number is: {count}")

main()