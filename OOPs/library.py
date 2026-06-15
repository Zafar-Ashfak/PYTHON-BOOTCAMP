# Create a Library class with:
# Object attributes: title, author, is_issued
# Methods:
# issue_book()
# return_book()
# display_status()

class Library:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

    def issue_book(self):
        self.is_issued = True

    def return_book(self):
        self.is_issued = False

    def display_status(self):
        print("Book Status")
        print(f"\tTitle: {self.title}")
        print(f"\tAuthor: {self.author}")

        if self.is_issued:
            print("\tBook is issued")
        else:
            print("\tBook is available to issue")

        print()


# Creating objects of class Library
book1 = Library("Rich Dad Poor Dad", "Robert T. Kiyosaki")
book1.display_status()

book2 = Library("The Psychology Of Money", "Morgan Housel")
book2.display_status()