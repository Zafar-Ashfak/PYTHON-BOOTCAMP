# Create a Circle class with:
#
# Object attribute: radius
# Methods:
# area()
# circumference()

import math

class Circle:
    def __init__(self, r):
        print(f"Circle with radius {r}m")
        self.r = r

    def area(self):
        return math.pi * self.r * self.r

    def circumference(self):
        return 2 * math.pi * self.r

    def display_info(self):
        print(f"Area of the circle is: {self.area():.2f}m²")
        print(f"Circumference of the circle is: {self.circumference():.2f}m\n")

# Creating objects of class Circle

c1 = Circle(15)
c1.display_info()

c2 = Circle(6)
c2.display_info()

c3 = Circle(30)
c3.display_info()

