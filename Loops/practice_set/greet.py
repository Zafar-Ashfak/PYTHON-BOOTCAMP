# Write a Python program that iterates through a list of names and prints a greeting only for
# those names that start with the letters 'R' or 'A'.

l = ["Rahbar", "Irfan", "Ashfaq", "Saba", "Zoya" ,"Ruhul", "Aftab", "Isha", "Anwar", "Mukhtar", "Fazil", ""]

for name in l:
    if name.startswith('R') or name.startswith('A'):
        print(f"Hello, {name}!")