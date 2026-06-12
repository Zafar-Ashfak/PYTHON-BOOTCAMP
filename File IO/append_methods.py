# Write a program that asks the user for some text and appends it to a file.
text = input("Enter some texts: ")

# append method
file = open("myfile.txt", "a")
file.write(f"{text}\n")
file.close()
