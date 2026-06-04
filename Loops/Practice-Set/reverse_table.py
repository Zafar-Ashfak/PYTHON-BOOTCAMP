print("Program to print table in reverse order")
n = int(input("Enter a natural number: "))

for i in reversed(range(1, 11)):
    print(f"{n} X {i} = {n * i}")