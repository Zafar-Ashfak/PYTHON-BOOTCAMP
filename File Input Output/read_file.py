"""
    "r" → Read (default)
    "w" → Write (creates new file or overwrites)
    "a" → Append (adds data at end)
    "x" → Create file (error if already exists)
    "b" → Binary mode
    "t" → Text mode (default)
"""

# file = open("story.txt", "r")
file = open("story.txt") # we can skip "r" mode for read file
data = file.read()
print(data)
file.close()

