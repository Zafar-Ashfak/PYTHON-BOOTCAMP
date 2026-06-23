# 3. Rectangle Class
#
# Create a Rectangle class with:
#
# Object attributes: length, breadth
# Method: area()
#
# Print the area of different rectangles.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


# Creating objects of class Rectangle
r1 = Rectangle(15, 7)
res = r1.area()
print(f"Area of the rectangle is: {res}")

r2 = Rectangle(20, 13)
res = r2.area()
print(f"Area of the rectangle is: {res}")

