animals = ["Cat", "Dog", "Elephant", "Horse", "Lion", "Tiger", "Zebra", "Giraffe", "Monkey"]

user_input = input("Enter an animal name: ")

user_input =user_input.capitalize()

if animals.__contains__(user_input):
    print(f"{user_input} contains in the list")
else:
    print(f"{user_input} doesn't contains in the list")

