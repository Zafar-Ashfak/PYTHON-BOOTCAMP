# Write a function sum_of_even_odd_digits(num) and print the sum of even and odd numbers
def sum_of_even_odd_digits(num):
    even = 0
    odd = 0
    while num > 0:
        rem = num % 10
        if rem % 2 == 0:
            even += rem
        else:
            odd += rem

        num //= 10

    print(f"Sum of all even integer is: {even}")
    print(f"Sum of all odd integer is: {odd}")


def main():
    print("Program to display sum of even and odd numbers")
    num = int(input("Enter a number: "))
    sum_of_even_odd_digits(num)

main()

