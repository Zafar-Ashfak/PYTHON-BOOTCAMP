# Write a program to create a new file that contains
# all non-empty lines from another file.

with open("crow.txt", "r") as src:
    lines = src.readlines()

with open("newfile.txt", "w") as new_file:
    for line in lines:
        if line.strip():  # Check if the line is not empty
            new_file.write(line)

print("Non-empty lines copied successfully.")