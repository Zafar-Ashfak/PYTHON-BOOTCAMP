# Create a Fan class with:
#
# Object attributes: brand, speed
# Method: change_speed(new_speed)

class Fan:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def change_speed(self, new_speed):
        if new_speed >= 0:
            self.speed = new_speed
        else:
            print("Speed cannot be negative")

    def show_speed(self):
        return self.speed

# Creating Objects of the class Fan
f1 = Fan("Usha", 240)
print(f"Fan brand: {f1.brand}, speed: {f1.speed}")

ns = int(input("Enter new speed: "))
f1.change_speed(ns)
print(f"After changing speed now fan's speed is: {f1.show_speed()}")