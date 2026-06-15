import os

# Select the directory path
path = "/"

# Get the list of files and folders
contents = os.listdir(path)
print("Contents of the directory:")

for item in contents:
    print(item)