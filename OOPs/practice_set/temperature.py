# Create a Temperature class with:
#
# Object attribute: Celsius
# Methods:
# to_fahrenheit()
# to_kelvin()

class Temperature:
    def __init__(self, celsius):
        if celsius < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")

        self.celsius = celsius

    def to_fahrenheit(self):
        return 9/5 * self.celsius + 32

    def to_kelvin(self):
        return self.celsius + 273.15

    def display_temperature(self):
        print(f"Temperature: {self.celsius}°C")
        print(f"{self.celsius}°C = {self.to_fahrenheit():.2f}°F")
        print(f"{self.celsius}°C = {self.to_kelvin()} K\n")

# Creating objects of class Temperature

t1 = Temperature(25)
t1.display_temperature()

t2 = Temperature(40)
t2.display_temperature()


