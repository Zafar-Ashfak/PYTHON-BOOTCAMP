# Write a program to calculate the sum of digits of a number using recursion
def sum_of_digits(n):
    # Base Case
    if n == 0:
        return 0
    # Work
    rem = n % 10
    return rem + sum_of_digits(n // 10)

def main():
    print("Program to calculate the sum of digits of a number")
    n = int(input("Enter a number: "))
    res = sum_of_digits(n)
    print(f"Sum of digits of {n} is: {res}")

main()
