# Write a program to wipe out the content of a file using python

with open("10_problem10.txt", "r") as file:
     print(file.read())

with open("10_problem10.txt", "w") as wipe_file:
    data = wipe_file.write(" ")
    print("\nContent deleted successfully")

with open("10_problem10.txt", "r") as check_file:
     print(check_file.read())