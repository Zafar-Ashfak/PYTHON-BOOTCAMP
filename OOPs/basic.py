class Student:

    # create one time in the memory
    college_name = "Massachusetts Institute of Technology" # class attribute

    def __init__(self, name, marks): # Constructor
        self.name = name # obj attribute
        self.marks = marks # obj attribute
        print("Adding student in the database...")

s1 = Student("Sidra Fatima", 99.4)
print(f"Student Name: {s1.name}\nMarks: {s1.marks}\n{s1.college_name}")

s2 = Student("Jarun Jawed", 86.8)
print(f"Student Name: {s1.name}\nMarks: {s1.marks}\nCollege Name: {s1.college_name}")

