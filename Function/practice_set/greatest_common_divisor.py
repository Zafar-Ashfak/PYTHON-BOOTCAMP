def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    print("Program to find out greatest common divisor of two numbers")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The greatest common divisor (GCD) =", gcd(num1, num2))

main()