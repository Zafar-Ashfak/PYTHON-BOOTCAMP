# Write a program to count the total number of lines in a file
with open("python.txt", "r") as file:
    count = 0
    for line in file:
        count += 1

print(f"Total number of lines in the file is: {count}")