# Write a program to check whether two files have exactly the same content.
def compare_files(file1, file2):
    with open(file1, "r") as f1:
        data1 = f1.read()

    with open(file2, "r") as f2:
        data2 = f2.read()

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