num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

if num1 == num2:
    print("Both numbers are equal")
elif num1 > num2:
    print(f"{num1} is largest number among: {num1} and {num2}")
else:
    print(f"{num2} is largest number among: {num1} and {num2}")