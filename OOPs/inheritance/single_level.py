class Animal:
    def __init__(self, skin_color):
        self.skin_color = skin_color

    def eat(self):
        print("Animal eats.")


class Fish(Animal):
    def swim(self):
        print("Fish swims.")


shark = Fish("Gray")

print(f"Shark's skin color is: {shark.skin_color}")
shark.eat()
shark.swim()