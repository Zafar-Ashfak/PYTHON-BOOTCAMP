# Write a program that reads a file contents and change it into uppercase and append in the same file.

with open("aladdin.txt", "r") as file:
    data = file.read()

with open("aladdin.txt", "a") as uppercase:
    uppercase.write(f"\n\n{data.upper()}")
    print("Converted to uppercase and appended successfully")
