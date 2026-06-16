# Write a program to display multiplication table of a given number using while loop

n = int(input("Enter a number for which you want the multiplication table: "))

i = 1
while i <= 10:
    print(f"{n} X {i} = {n * i}")
    i += 1

