from abc import ABC, abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def honk(self):
        pass


class Car(Vehicle):
    def __init__(self, color, wheels, brand, top_speed, fuel_type):
        self.color = color
        self.wheels = wheels
        self.brand = brand
        self.top_speed = top_speed
        self.fuel_type = fuel_type

    def mileage(self):
        print("Mileage: 12km/l")

    def start(self):
        print("Car started...")

    def stop(self):
        print("Car stopped...")

    def brake(self):
        print("Applied brake")

    def honk(self):
        print("Beep Beep!")

class SuperCar(Car):
    def __init__(self, color, wheels, brand, top_speed, fuel_type):
        super().__init__(color, wheels, brand, top_speed, fuel_type)

    def drive_type(self):
        print("Can drive, RWD or AWD")


def main():
    # Creating object of class SuperCar
    p1 = SuperCar("Red", 4, "Pagani", "400km/h", "Petrol")
    print(f"Super Car Brand: {p1.brand}")
    print(f"Color: {p1.color}")
    print(f"Speed: {p1.top_speed}")
    print(f"Fuel Type: {p1.fuel_type}")
    p1.drive_type()
    p1.mileage()
    p1.start()
    p1.honk()
    p1.brake()
    p1.stop()

main()