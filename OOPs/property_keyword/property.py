class Student:
    college = "MANUU"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_percentage(self):
        s = 0
        for e in self.marks:
            s += e

        print(f"Total percentage: {s / 3}%")


def main():
    s1 = Student("Saba Anjum", [99, 94, 97])
    s1.get_percentage()

    s1.marks[1] = 95
    s1.get_percentage()

main()