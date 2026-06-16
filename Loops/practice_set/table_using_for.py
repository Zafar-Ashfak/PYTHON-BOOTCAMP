# Write a program to display multiplication table of a given number using for loop

table = int(input("Enter a number for which you want the multiplication table: "))

for i in range(1, 11):
    print(f"{table} X {i} = {table * i}")
