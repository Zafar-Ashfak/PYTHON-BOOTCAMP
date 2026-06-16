# Write a function sum_natural(n) that returns the sum of the first n natural numbers.

def sum_natural(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

def main():
    print("Program to display sum of the first n natural numbers")
    n = int(input("Enter a natural number: "))
    res = sum_natural(n)
    print(f"Sum of first {n} natural number is: {res}")

main()
