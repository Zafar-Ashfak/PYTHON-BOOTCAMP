animals = ["Cat", "Dog", "Elephant", "Horse", "Lion", "Tiger", "Zebra", "Giraffe", "Monkey"]

name = input("Enter an animal name: ")

name = name.capitalize()

if name in animals:
    print(f"Yes, {name} is in the list")
else:
    print(f"No, {name} is not in the list")

