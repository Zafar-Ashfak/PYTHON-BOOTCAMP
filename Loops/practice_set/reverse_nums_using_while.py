# Write a program to print numbers from n to 1 in reverse order by user's choice using while loop

print("Program to print natural number from n to 1")
n = int(input("Enter a natural number: "))

while n >= 1:
    print(n, end= " ")
    n -= 1