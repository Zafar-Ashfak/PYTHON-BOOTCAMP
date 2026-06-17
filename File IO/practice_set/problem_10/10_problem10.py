# Write a program that reads content of a file and wipe out.

with open("wiped_file.txt", "r") as file:
     print(file.read())

with open("wiped_file.txt", "w") as wiped_file:
    data = wiped_file.write(" ")
    print("\nContent deleted successfully")

with open("wiped_file.txt", "r") as check_file:
     print(check_file.read())