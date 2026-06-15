num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
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
elif operator == '**':
    print(f"{num1} ** {num2} = {num1 ** num2}")
elif operator == '//':
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(f"{num1} // {num2} = {num1 // num2}")

else:
    print("Invalid operator, please try again!")