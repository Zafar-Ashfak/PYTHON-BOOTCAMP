text = input("Enter a message for us: ")

file = open("myfile.txt", "w")
file.write(text)
file.close()