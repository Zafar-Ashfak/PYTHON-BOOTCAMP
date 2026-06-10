# Find the product of two numbers using recursion (without using *)
def product(a, b):
    # Base Case
    if b == 0:
        return 0

    # Handle negative integer
    if b < 0:
        return -product(a, -b)

    # Recursion Call
    return a + product(a, b - 1)

def main():
    print("Program to find the product of two numbers using recursion (without using *)")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    res = product(a, b)
    print(f"{a} X {b} = {res}")

main()