# Create a Counter class with:
#
# Class attribute: count = 0
# Increment count every time a new object is created.
# Method: show_count()

class Counter:
    count = 0
    def __init__(self):
        print("Object is created...")
        Counter.count += 1

    def show_count(self):
        print(f"Count: {Counter.count}\n")


# Creating objects of class Counter

c1 = Counter()
c1.show_count()

c2 = Counter()
c2.show_count()

c3 = Counter()
c3.show_count()

c4 = Counter()
c4.show_count()
