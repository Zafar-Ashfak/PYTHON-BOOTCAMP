# Take Nothing Return Something
import math
def get_area():
    r = int(input("Enter the radius of the circle: "))
    return math.pi * r * r

area = get_area()
print(f"Area of the circle is: {area}")