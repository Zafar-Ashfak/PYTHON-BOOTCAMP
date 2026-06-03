num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 == num2 == num3:
    print("All numbers are equal")
elif num1 > num2 and num1 > num3:
    print(f"{num1} is the largest number among: {num1}, {num2} and {num3}")
elif num2 > num3:
    print(f"{num2} is the largest number among: {num1}, {num2} and {num3}")
else:
    print(f"{num3} is the largest number among: {num1}, {num2} and {num3}")