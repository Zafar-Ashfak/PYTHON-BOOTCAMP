import datetime

name = input("Enter your name: ")

# print("Good Afternoon", name)

print(f"Good Afternoon {name}")

letter = f'''
    Dear {name},
    You are selected!
    {datetime.datetime.now()}
'''

print(letter)