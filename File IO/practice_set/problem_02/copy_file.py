# Write a program to copy the contents of a file from source.txt to destination.txt.
with open("src.txt", "r") as file:
    data = file.read()

with open("dest.txt", "w") as copy_file:
    copy_file.write(data)
    print("Contents copied successfully")