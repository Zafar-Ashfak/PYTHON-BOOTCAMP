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