# Write a program to print table in reverse order

print("Program to print table in reverse order")
n = int(input("Enter a natural number: "))

print("Prints table using step size")
for i in range(10, 0, -1):
    print(f"{n} X {i} = {n * i}")

print("\nPrints table using reversed method")

for j in reversed(range(1, 11)):
    print(f"{n} X {j} = {n * j}")