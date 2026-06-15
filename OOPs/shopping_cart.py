# Create a ShoppingCart class with:
#
# Object attribute: items (a list)
# Methods:
# add_item(item)
# remove_item(item)
# display_items()

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not found")

    def display_items(self):
        print(f"Cart Items:")
        for item in self.items:
            print(f" - {item}")

        print()


# Creating objects of class ShoppingCart
s1 = ShoppingCart()
s1.add_item("Vegetables")
s1.add_item("Rice")
s1.add_item("Pulse")
s1.add_item("Sugar")
s1.add_item("Fruits")
s1.add_item("Dishes")
s1.display_items()

s1.remove_item("Dishes")
print("\nAfter removing Dishes")
s1.display_items()


s1.remove_item("Banana")
s1.display_items()
