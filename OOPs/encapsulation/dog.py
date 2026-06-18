# Create a Dog class with:
#
# Class attribute: species = "Dog"
# Object attributes: name, age
# Methods:
# bark()
# display_info()

class Dog:
    species = "Dog"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof woof!")

    def display_info(self):
        print(f"Dog name: {self.name}, age: {self.age} years")


# Creating objects of class Dog
d1 = Dog("Siberian Husky", 13)
print(f"Species: {d1.species}")
d1.display_info()
d1.bark()

print()

d2 = Dog("BullDog", 8)
print(f"Species: {d2.species}")
d2.display_info()
d2.bark()