# Write a function is_prime(num) and returns True if prime or return false otherwise.
import math
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def main():
    print("Program to display a number is prime or not")
    num = int(input("Enter a natural number: "))
    if is_prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

main()