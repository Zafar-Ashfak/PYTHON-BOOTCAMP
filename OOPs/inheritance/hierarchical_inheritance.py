class Animal:
    def __init__(self, skin_color):
        self.skin_color = skin_color

    def eat(self):
        print("Eats")

    def breathe(self):
        print("Breathes in the air")

    def habitat(self):
        pass

class Herbivores(Animal):
    def eat(self):
        print("Eats grasses, leaves, plants etc.")

    def habitat(self):
        print("Lives in the shelter")

class Carnivorous(Animal):
    def eat(self):
        print("Eats fleshes of other animals")

    def habitat(self):
        print("Lives in the forest")

class Omnivorous(Animal):
    def eat(self):
        print("Eats both plants and flesh of other animals.")

    def habitat(self):
        print("Lives in the forest")

def main():
    # Creating objects of class Herbivores
    cow = Herbivores("Black, Red or White")
    print("Herbivorous Animal\nName: Cow")
    print(f"Skin color: {cow.skin_color}")
    cow.eat()
    cow.breathe()
    cow.habitat()

    print()

    # Creating objects of class Carnivorous
    lion = Carnivorous("Golden yellow")
    print("Carnivorous Animal\nName: Lion")
    print(f"Skin color: {lion.skin_color}")
    lion.eat()
    lion.breathe()
    lion.habitat()

    print()

    # Creating objects of class Omnivorous
    bear = Omnivorous("Brown or White")
    print("Omnivorous Animal\nName: Bear")
    print(f"Skin color: {bear.skin_color}")
    bear.eat()
    bear.breathe()
    bear.habitat()


main()