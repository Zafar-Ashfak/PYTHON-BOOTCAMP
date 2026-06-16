birds = ["Parrot", "Peacock", "Peahen", "Crow", "Sparrow", "Hen", "Cock", "Cuckoo", "Nightingale"]

name = input("Enter a bird name: ")

name = name.capitalize()

if name in birds:
    print(f"Yes, {name} is in the list")
else:
    print(f"No, {name} is not in the list")

