# Create a LightBulb class with:
#
# Object attribute: is_on
# Methods:
# turn_on()
# turn_off()

class LightBulb:
    def __init__(self, is_on):
        self.is_on = is_on

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on:
            print("Bulb is turned on")
        else:
            print("Bulb is turned off")


# Creating Objects of class LightBulb
print("First bulb")
bulb1 = LightBulb(True)
bulb1.turn_off()
bulb1.show_status()

print("\nSecond bulb")
bulb2 = LightBulb(False)
bulb2.turn_on()
bulb2.show_status()


