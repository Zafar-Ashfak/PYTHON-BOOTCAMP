# Write a function largest(a, b) that returns the larger of two numbers.
print("Program to display largest of two numbers")
def largest(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"Largest number is: {largest(num1, num2)}")