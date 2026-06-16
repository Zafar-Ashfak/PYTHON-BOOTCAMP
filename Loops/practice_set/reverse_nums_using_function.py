# Write a program to print numbers from n to 1 in reverse order by user's choice using for loop

print("Program to print numbers from n to 1")
n = int(input("Enter a natural numbr: "))

for i in reversed(range(1, n + 1)):
    print(i, end=" ")