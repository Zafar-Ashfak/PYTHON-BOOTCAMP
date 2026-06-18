class Student:
    college = "Netaji Subhas University of Technology, Delhi"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def greet():
        print("Good morning,", end=" ")

    def get_department(self):
        print(f"{self.name}, you have been assigned to the Computer Science department.")


# Creating an object of the Student class
student1 = Student("Shraddha Khapra", 93)

student1.greet()
print(student1.name)
student1.get_department()

# Demonstrating the del keyword
del student1.name    # Deletes the name attribute
del student1.marks   # Deletes the marks attribute
del student1         # Deletes the object reference

# Uncommenting the following lines will raise a NameError
# because student1 no longer exists.

# student1.greet()
# print(student1.name)
# student1.get_department()