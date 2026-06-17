# Write a program to check whether two files have exactly the same content.
def compare_files(f1, f2):
    with open(f1, "r") as file1:
        data1 = file1.read()

    with open(f2, "r") as file2:
        data2 = file2.read()

        return data1 == data2


def main():
    print("Program to check whether two files have exactly the same content")
    file1 = "file1.txt"
    file2 = "file2.txt"

    if compare_files(file1, file2):
        print("Yes, both files have exactly same contents")
    else:
        print("No, both files have not same contents")

main()