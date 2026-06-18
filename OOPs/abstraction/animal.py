# Here are more abstract method ideas you can choose from:

# Method	Purpose
# make_sound()	Animal's sound (Bark, Meow, Roar)
# move()	How it moves (Run, Fly, Swim)
# eat()	How it eats
# sleep()	Sleeping behavior

from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self):
        print("Animal constructor called...")

    @staticmethod
    def sleep():
        print("Animal sleeps")

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def habitat(self):
        pass


class Cat(Animal):
    def __init__(self):
        super().__init__()
        print("Cat constructor called...")


    def eat(self):
        print("Cat eats milk and meat")

    def move(self):
        print("Cats move on four legs")

    def make_sound(self):
        print("Cats make meow, meow sound")

    def habitat(self):
        print("Cats live in homes")

class Bear(Animal):
    def __init__(self):
        super().__init__()
        print("Bear constructor is called...")

    def eat(self):
        print("Bears eat honey and fishes")

    def move(self):
        print("Bears move on two legs.")

    def make_sound(self):
        print("Bears roar.")

    def habitat(self):
        print("Bears live in the forest")

# Creating object of class Cat
kitty = Cat()
kitty.sleep()
kitty.eat()
kitty.move()
kitty.make_sound()
kitty.habitat()

print()

# Creating object of class Bear
baloo = Bear()
baloo.sleep()
baloo.eat()
baloo.move()
baloo.make_sound()
baloo.habitat()


