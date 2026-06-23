class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price

    def __str__(self):
        return f"Item: {self.item}, price: {self.price}"

def main():
    # Creating objects of class Order
    order1 = Order("Xbox", 42999)
    order2 = Order("PS5", 49999)

    print(order1)
    print(order2)
    if order1 > order2:
        print("Order1 is costlier than order2")
    else:
        print("Order2 is costlier than order1")


main()