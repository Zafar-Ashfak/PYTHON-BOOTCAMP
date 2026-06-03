num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator: ")

if operator == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == '*':
    print(f"{num1} X {num2} = {num1 * num2}")
elif operator == '/':
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
elif operator == '%':
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(f"{num1} % {num2} = {num1 % num2} (remainder)")
else:
    print("Invalid operator, please try again!")