class Student:
    college = "MANUU"

    def __init__(self, name, phy, che, math):
        self.name = name
        self.phy = phy
        self.che = che
        self.math = math
        # self.percentage = f"{(self.phy + self.che + self.math) / 3:.2f} %"

    @property
    def percentage(self):
        return f"{(self.phy + self.che + self.math) / 3:.2f} %"


def main():
    s1 = Student("Saba Anjum", 99, 94, 97)
    print(f"Student Name: {s1.name}")
    print(f"College: {s1.college}")
    print(f"Marks: {s1.percentage}")

    print("After changing marks in physics")
    s1.math = 98
    print(f"Final Marks: {s1.percentage}")



main()