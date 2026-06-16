print("Program to print whether a given number is prime or not")
n = int(input("Enter a natural number: "))

is_prime = True

if n < 2:
    is_prime = False

for i in range(2, n):
    if n % i == 0:
        is_prime = False


if is_prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")