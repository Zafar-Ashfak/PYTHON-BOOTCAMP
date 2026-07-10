# Write a Python program that accepts a user's name as input, greets the user,
# and prints a personalized letter along with the current date and time.
import datetime

name = input("Enter your name: ")

# print("Good Afternoon", name) using traditional way

print(f"Good Afternoon {name}") # using f string way

letter = f'''
    Dear {name},
    You are selected!
    {datetime.datetime.now()}
'''

print(letter)