message = input("Enter a message: ")

# append method
file = open("myfile.txt", "a")
file.write(f"{message}\n")
file.close()
