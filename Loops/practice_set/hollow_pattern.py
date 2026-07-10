# Write a program that prints hollow pattern program for n height given by user

print("Program to print hollow pattern program by user's choice")
n = int(input("Enter a natural number: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or j == 1 or i == n or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()