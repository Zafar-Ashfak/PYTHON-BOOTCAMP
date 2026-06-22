# Animal -> Horse -> Mustang
# Animal -> Fish -> Shark
# Animal -> Bird -> Eagle, Duck

class Animal:
    def __init__(self, skin_color):
        self.skin_color = skin_color

    def eat(self):
        print("Eats")

    def breathe(self):
        print("Breathes")

class Horse(Animal):
    def __init__(self, leg, skin_color):
        super().__init__(skin_color)
        self.leg = leg

    def run(self):
        print("Runs on the ground")

    def habitat(self):
        print("Lives in the horse barn")

    def eat(self):
        print("Eat grasses, plants and branches of the tree")

    def breathe(self):
        print("Breathe in the air")

class Mustang(Horse):
    def __init__(self, leg, skin_color):
        super().__init__(leg, skin_color)

    def strength(self):
        print("Fastest and strongest horse in the breed")


def main():
    # Creating object of class Mustang
    m1 = Mustang(4, "Bay, Black and Chestnut")
    print("Animal name: Horse")
    print(f"Skin color: {m1.skin_color}")
    print(f"Legs: {m1.leg}")
    m1.strength()
    m1.run()
    m1.habitat()
    m1.eat()
    m1.breathe()


main()