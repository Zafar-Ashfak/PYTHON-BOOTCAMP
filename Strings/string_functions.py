name = "   hello i am a senior software  engineer    "

print("Length of the string is:", len(name))

print(name.startswith("Za")) # True

print(name.endswith("aq")) # True

print(name.capitalize()) # Capitalize the first char of the string

print(name.lower()) # Converts to lowercase

print(name.upper()) # Converts to uppercase

print(name.title())  # Capitalizes each word

print("Letter 'a' occurs", name.count("a"), "times in the given string")

print(name.strip()) # Removes spaces from both ends

print(name.lstrip()) # Removes spaces from left side

print(name.rstrip()) # Removes spaces from right side

print("Letter 'i' occurs at index", name.find('i'), "from end") # Find the char from end

print(name.replace('senior', 'junior'))

print(name.split()) # Splits string into list