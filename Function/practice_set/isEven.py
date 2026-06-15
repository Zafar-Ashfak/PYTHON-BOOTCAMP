def iseven(n):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input("Enter a natural number: "))
if iseven(num):
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")