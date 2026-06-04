print("Program to print whether a given number is prime or not")
n = int(input("Enter a natural number: "))

isPrime = True

if n < 2:
    isPrime = False

for i in range(2, n):
    if n % i == 0:
        isPrime = False


if isPrime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")