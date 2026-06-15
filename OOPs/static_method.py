class Employee:
    company = "Google"

    def __init__(self, name):
        self.name = name

    @staticmethod # decorator
    def greet():
        print(f"Welcome to {Employee.company}", end= " ")


e1 = Employee("Zafar Ashfak")
Employee.greet() # Calling static method
print(e1.name)