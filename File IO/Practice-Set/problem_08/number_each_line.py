# Write a program that reads a file and writes each line prefixed with its line number.
def number_each_line(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "a") as file:
        num = 1

        file.write("\n\nLines with numbering\n\n")
        for line in lines:
            file.write(f"{num}. {line}")
            num += 1

        print("Numbering completed successfully")


def main():
    print("Program that reads a file and writes each line prefixed with its line number")
    filename = "file.txt"
    number_each_line(filename)

main()
