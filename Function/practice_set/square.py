# Write a function square(n) that returns the square of a given number.
def square(n):
    return n ** 2

num = int(input("Enter a natural number: "))
print(f"{num} ** 2 = {square(num)}")
