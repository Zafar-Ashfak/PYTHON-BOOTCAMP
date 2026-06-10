# Write a program to generate the nth Fibonacci number
def fibonacci(n):
    # Base Case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursion Call
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    print("Program to generate the nth Fibonacci number")
    n = int(input("Enter a natural number: "))
    res = fibonacci(n)
    print(f"{n}th fibonacci number is: {res}")

main()