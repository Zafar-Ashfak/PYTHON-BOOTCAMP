# Write a program to merge the contents of two files into a third file.

def merge_files(file1, file2, file3):
    with open(file1, "r") as f1:
        data1 = f1.read()

    with open(file2, "r") as f2:
        data2 = f2.read()


    with open(file3, "w") as f3:
        f3.write(data1)
        f3.write("\n\n")
        f3.write(data2)
        print("Contents of two files have merged successfully")

def main():
    print("Program to merge the contents of two files into a third file")
    file1 = "file1.txt"
    file2 = "file2.txt"
    file3 = "file3.txt"

    merge_files(file1, file2, file3)

main()