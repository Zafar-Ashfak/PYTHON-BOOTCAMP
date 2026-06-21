class Animal:
    def __init__(self, skin_color):
        self.skin_color = skin_color

    def eat(self):
        print("Eats")

    def breathe(self):
        print("breathes in the air")

class Mammal(Animal):
    def __init__(self, leg, skin_color):
        super().__init__(skin_color)
        self.leg = leg

    def walk(self):
        print("Walks on the land")

class Dog(Mammal):
    def __init__(self, breed, skin_color, leg):
        super().__init__(leg, skin_color)
        self.breed = breed

    def eat(self):
        print("Eats bones, flesh, bread and many things.")

    def run(self):
        print("Run on 4 legs")

def main():
    # Creating object of class Dog
    dobby = Dog("BullDog", "Brown", 4)
    print(f"Dog breed: {dobby.breed}")
    print(f"Skin color: {dobby.skin_color}")
    dobby.run()
    dobby.walk()
    dobby.eat()
    dobby.breathe()


main()

