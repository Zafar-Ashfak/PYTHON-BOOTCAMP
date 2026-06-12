# Write a program to count the total number of characters in file
with open("python.txt", "r") as file:
    data = file.read()
    count = 0
    for char in data:
        count += 1

    print(f"Total number of characters in the file 'file.txt' is: {count}")

