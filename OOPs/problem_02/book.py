# 2. Book Class
#
# Create a Book class with:
#
# Object attributes: title, author, price
# Method: display_book()
#
# Create a few books and display their details.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_book(self):
        print("Book Information:")
        print(f"\tTitle: {self.title}")
        print(f"\tauthor: {self.author}")
        print(f"\tPrice: {self.price} rupees")


# Creating Book Objects
b1 = Book("The Psychology Of Money", "Morgan Housel", 380)
b1.display_book()

print()

b2 = Book("Rich Dad Poor Dad", "Robert T. Kiyosaki", 410)
b2.display_book()

print()

b3 = Book("The Power Of your Subconscious Mind", "Joseph Murphy", 290)
b3.display_book()

print()

b4 = Book("Atomic Habits", "James Clear", 300)
b4.display_book()

print()

b5 = Book("Harry Potter", "J.K. Rowling", 530)
b5.display_book()
