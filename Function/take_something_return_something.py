# Take Something Return Something
def division(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"

    return num1 / num2

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"{a} / {b} = {division(a, b)}")