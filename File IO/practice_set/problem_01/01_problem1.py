# Write a program to read user's name from a given file 'names.txt' and find whether it contains or not.

name = input("Enter your full name here: ").lower()

with open("names.txt") as file:
    data = file.read().lower().splitlines()

    if name in data:
        print("Name found")
    else:
        print("Name not found")
