# Write a program to copy the contents of source.txt into destination.txt.
with open("source.txt", "r") as file:
    data = file.read()

with open("dest.txt", "w") as copy_file:
    copy_file.write(data)
    print("Contents copied successfully")