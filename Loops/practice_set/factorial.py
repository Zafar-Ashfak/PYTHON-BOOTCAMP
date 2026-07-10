# Write a Python program to print factorial of a given number

print("Program to print factorial of a given number n")
n = int(input("Enter a number: "))
factorial = 1
for i in range (1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")