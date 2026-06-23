class Employee:
    company = "Amazon"

    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show_details(self):
        print(f"Role: {self.role}")
        print(f"Salary: {self.salary} LPA")
        print(f"Company: {self.company}")


class Engineer(Employee):
    def __init__(self, name, age, role, department, salary):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Age: {self.age}")
        super().show_details()
        print()

# Creating Student objects
e1 = Engineer("Saba Zafar", 25,"Transportation Specialist", "Supply Chain", 450000)
e1.show_details()

e2 = Engineer("Zafar Ashfaq", 27, "Java Backend Developer", "Software Development", 3400000)
e2.show_details()
