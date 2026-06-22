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

class Fish(Animal):
    def __init__(self, fins, skin_color):
        super().__init__(skin_color)
        self.fins = fins

    def swim(self):
        print("Swims in the water")

    def habitat(self):
        print("Lives in the water")

class Shark(Fish):
    def __init__(self, teeth, fins, skin_color):
        super().__init__(fins, skin_color)
        self.teeth = teeth

    def strength(self):
        print("Bigger and Stronger fish in the breed")

    def eat(self):
        print("Eat small fish")

    def breathe(self):
        print("Breathe in the water through gills")



class Bird(Animal):
    def __init__(self, wings, skin_color):
        super().__init__(skin_color)
        self.wings = wings

    def fly(self):
        print("Flies in the sky")

    def habitat(self):
        print("Lives on the branches of the tree")


class Eagle(Bird):
    def __init__(self, wings, skin_color):
        super().__init__(wings, skin_color)

    def strength(self):
        print("Can fly high in the sky")

    def eat(self):
        print("Eat flesh of dead animals")

    def breathe(self):
        print("Breathe in the air")


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

    # Creating object of class Shark
    s1 = Shark(300, 8, "Gray")
    print("\n\nAnimal name:  Shark")
    print(f"Skin color: {s1.skin_color}")
    print(f"Teeth: {s1.teeth}")
    print(f"Fins: {s1.fins}")
    s1.strength()
    s1.swim()
    s1.habitat()
    s1.eat()
    s1.breathe()

    # Creating object of class Shark
    e1 = Eagle(2, "Black")
    print("\n\nAnimal name:  Eagle")
    print(f"Skin color: {e1.skin_color}")
    print(f"Wings: {e1.wings}")
    e1.strength()
    e1.fly()
    e1.habitat()
    e1.eat()
    e1.breathe()





main()