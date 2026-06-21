class Animal:
    def eat(self):
        print("Eats")

    def breathe(self):
        print("breathes")

class LandAnimal(Animal):
   def walk(self):
       print("Walks on the land")

class WaterAnimal(Animal):
    def swim(self):
        print("Swims in the water")

class Turtle(LandAnimal, WaterAnimal):
    pass


def main():
    # Creating object of class Turtle
    print("Land and Water animal: Turtle")
    tuck = Turtle()
    tuck.eat()
    tuck.breathe()
    tuck.walk()
    tuck.swim()

main()