# Write a program to print numbers from n to 1 by user's choice using for loop

print("Program to print numbers from n to 1")
n = int(input("Enter a natural number: "))

for i in range(n, 0, -1):
    print(i, end=" ")   