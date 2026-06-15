num1 = input("Enter an integer number: ")
num2 = input("Enter an float number: ")

check1 = type(num1)

print("Before type casting input type is: ", check1)

num1 = int(num1)
check1 = type(num1)
print("After type casting input type is: ", check1)

print("\n")

check2 = type(num2)
print("Before type casting input type is: ", check2)
num2 = float(num2)
check2 = type(num2)
print("After type casting input type is: ", check2)