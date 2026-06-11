# Write in file using with keyword
message = input("Enter a message: ")
with open("file.txt", "w") as w_file:
    w_file.write(message)
    # No need to close the file using close() method

# Read data from file using with keyword
with open("file.txt", "r") as file:
    data = file.read()
    print(data)
    # No need to close the file using close() method




