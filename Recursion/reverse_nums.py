# Write a program to print numbers from n to 1 using recursion
def nums_reverse(n):
    # Base Case
    if n == 0:
        return

    # Work
    print(n, end=" ")
    nums_reverse(n - 1)

def main():
    print("Program to print numbers from n to 1")
    n = int(input("Enter a natural number: "))
    nums_reverse(n)

main()