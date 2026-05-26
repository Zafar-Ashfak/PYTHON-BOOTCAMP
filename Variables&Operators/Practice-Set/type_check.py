num = input("Enter a number: ")

check = type(num)

print("Before type casting input type is: ", check)

num = int(num)
check = type(num)
print("After type casting input type is: ", check)