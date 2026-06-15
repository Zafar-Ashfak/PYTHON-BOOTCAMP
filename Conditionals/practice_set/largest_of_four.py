num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))
num4 = int(input("Enter the 4th number: "))

if num1 == num2 == num3 == num4:
    print("All numbers are equal")
elif num1 > num2 and num1 > num3 and num1 > num4:
    print(f"{num1} is the largest number among: {num1}, {num2}, {num3} and {num4}")
elif num2 > num3 and num2 > num4:
    print(f"{num2} is the largest number among: {num1}, {num2}, {num3} and {num4}")
elif num3 > num4:
    print(f"{num3} is the largest number among: {num1}, {num2}, {num3} and {num4}")
else:
    print(f"{num4} is the largest number among: {num1}, {num2}, {num3} and {num4}")