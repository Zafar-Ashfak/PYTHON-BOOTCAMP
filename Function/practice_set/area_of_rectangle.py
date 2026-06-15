# Write a function rectangle_area(length, breadth) that returns the area of a rectangle.
print("Program to print area of the rectangle")
def rectangle_area(l, b):
    return l * b

length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))

print(f"Area: {rectangle_area(length, breadth)}")