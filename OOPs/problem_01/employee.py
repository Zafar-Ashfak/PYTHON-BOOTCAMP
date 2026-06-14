class Employee:
    company = "Google"

    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def display_info(self):
        print(f"Employee name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Salary: {self.salary} LPA")
        print(f"Company: {self.company}")


# Creating Student objects
e1 = Employee("Md Ashfak Alam", "Java Developer", 2700000)
e1.display_info()

e2 = Employee("Rahbar Hussain", "Python Full Stack Developer", 3400000)
e2.display_info()