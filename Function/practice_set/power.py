# Write a function power(base, exponent) that returns base raised to the power exponent.

def power(base, exponent):
    res = 1
    for i in range(exponent):
        res *= base

    return res

def main():
    print("Program to calculate the power of a number")
    b = int(input("Enter the base: "))
    e = int(input("Enter the exponent: "))
    print(f"{b} ** {e} = {power(b, e)}")

main()