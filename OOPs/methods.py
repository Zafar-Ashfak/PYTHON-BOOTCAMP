class Car:
    brand = "Pagani" # class attribute
    wheels = 4 # class attribute
    def __init__(self, color, engine):
        self.color = color # obj attribute
        self.engine = engine # obj attribute
        print("Car is created...")

    def change_color(self, color):
        self.color = color
        return color


c1 = Car("Red", "V8")
print(f"Brand: {c1.brand}")
print(f"Color: {c1.color}")
print(f"Engine: {c1.engine}")
print(f"Wheels: {c1.wheels}")

print(f"New color: {c1.change_color("Blue")}")



