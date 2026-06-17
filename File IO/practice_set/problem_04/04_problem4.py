# A file contains a word "Donkey" multiple times. You need to write a program which replace this word with "Horse" by updating the same file.

with open("donkey_story.txt", "r") as file:
    data = file.read()

    new_data = data.replace("Donkey", "Camel")

with open("donkey_story.txt", "w") as update_file:
    update_file.write(new_data)

print("File updated successfully\n")

with open("donkey_story.txt", "r") as read_file:
    print(read_file.read())