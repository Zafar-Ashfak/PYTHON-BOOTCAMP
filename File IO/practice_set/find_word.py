# Write a program that reads a file content and check whether the word "Python" exists in a file.
with open("python.txt", "r") as file:
    data = file.read().lower()
    word = "python"
    if word in data:
        print(f"Word {word} exists in the file")
    else:
        print(f"Word {word} doesn't exist in the file")
