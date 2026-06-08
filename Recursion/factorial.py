# Write a program to calculate factorial of a number using recursion
def factorial(n):
    # Base Case
    if n == 0 or n == 1:
        return 1

    # Work
    return n * factorial(n - 1)
def main():
    print("Program to calculate factorial of a number")
    n = int(input("Enter a number: "))
    res = factorial(n)
    print(f"{n}! = {res}")

main()