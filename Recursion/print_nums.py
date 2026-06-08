# Write a program to print numbers from 1 to n
def nums(n):
    # Base Case
    if n == 0:
        return

    # Work
    nums(n - 1)
    print(n, end=" ")

def main():
    print("Program to print numbers from 1 to n")
    n = int(input("Enter a natural number: "))
    nums(n)

main()