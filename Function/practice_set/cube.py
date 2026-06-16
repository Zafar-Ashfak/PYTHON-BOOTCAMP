# Write a function cube(n) that returns the cube of a given number.

def cube(n):
    return n * n * n

num = int(input("Enter a natural number: "))
print(f"{num} ^ 3 = {cube(num)}")