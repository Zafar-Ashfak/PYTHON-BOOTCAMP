# Write a program that reads a file content and count the total number of words in file
with open("python.txt", "r") as file:
    data = file.read()
    words = data.split() # splits string into list
    count = 0

    for word in words:
        count += 1

    print(f"Total number of words in the 'file.txt' is: {count}")