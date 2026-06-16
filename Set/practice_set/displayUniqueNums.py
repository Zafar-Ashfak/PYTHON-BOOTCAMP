# Write a program to take input from the user and display all the unique numbers (once).
num_set = set()

num = int(input("Enter the 1st number: "))
num_set.add(num)

num = int(input("Enter the 2nd number: "))
num_set.add(num)

num = int(input("Enter the 3rd number: "))
num_set.add(num)

num = int(input("Enter the 4th number: "))
num_set.add(num)

num = int(input("Enter the 5th number: "))
num_set.add(num)

num = int(input("Enter the 6th number: "))
num_set.add(num)

num = int(input("Enter the 7th number: "))
num_set.add(num)

num = int(input("Enter the 8th number: "))
num_set.add(num)

print(f"Display only unique values: {num_set}")