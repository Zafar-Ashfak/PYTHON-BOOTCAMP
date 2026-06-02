# Q(6). Create an empty dictionary. Allows 4 friends to enter their favorite language as value
# and use key as their names. Assume that the name is unique.
my_dict = {}

friend1 = input("Enter 1st friend name: ")
fav_lang1 = input("Enter your favorite language: ")
my_dict.update({friend1 : fav_lang1})

friend2 = input("Enter 2nd friend name: ")
fav_lang2 = input("Enter your favorite language: ")
my_dict.update({friend2 : fav_lang2})

friend3 = input("Enter 3rd friend name: ")
fav_lang3 = input("Enter your favorite language: ")
my_dict.update({friend3 : fav_lang3})

friend4 = input("Enter 4th friend name: ")
fav_lang4 = input("Enter your favorite language: ")
my_dict.update({friend4 : fav_lang4})


print(my_dict)

# Q(7). If name of the two friends are same, then what will happen in the program
# answer: If two friends have the same name, the second entry will overwrite the
#         first one because dictionary keys must be unique.

# Q(8). If languages of two friends are same, then what will happen in the program
# answer: If two friends have the same favorite language, nothing unusual happens because dictionary values can be duplicated.