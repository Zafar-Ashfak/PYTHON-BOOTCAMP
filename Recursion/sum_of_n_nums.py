# Write a program to calculate the sum of first n natural numbers
def sum_of_nums(n):
    s = 0
    # Base Case
    if n == 0:
        return 0

    # Work
    return n + sum_of_nums(n - 1)

def main():
    print("Program to calculate the sum of first n natural numbers")
    n = int(input("Enter a number: "))
    res = sum_of_nums(n)
    print(f"Sum of first {n} natural numbers is: {res}")
main()