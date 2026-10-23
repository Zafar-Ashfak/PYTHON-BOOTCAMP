# Write a Python program to check if a number is even or odd

def iseven(n : int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input("Enter a natural number: "))
if iseven(num):
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")