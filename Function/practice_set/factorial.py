# Write a function factorial(n) that returns the factorial of a number.

print("Program to calculate factorial of number n")
def factorial(n):
    fac = 1
    for i in range(n, 0, -1):
        fac *= i

    return fac


num = int(input("Enter a natural number: "))
print(f"{num}! = {factorial(num)}")