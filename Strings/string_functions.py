str = "   hello i am a senior software  engineer    "

print("Length of the string is:", len(str))

print(str.startswith("Za")) # True

print(str.endswith("aq")) # True

print(str.capitalize()) # Capitalize the first char of the string

print(str.lower()) # Converts to lowercase

print(str.upper()) # Converts to uppercase

print(str.title())  # Capitalizes each word

print("Letter 'a' occurs", str.count("a"), "times in the given string")

print(str.strip()) # Removes spaces from both ends

print(str.lstrip()) # Removes spaces from left side

print(str.rstrip()) # Removes spaces from right side

print("Letter 'i' occurs at index", str.find('i'), "from end") # Find the char from end

print(str.replace('senior', 'junior'))

print(str.split()) # Splits string into list


chars = "abcdefg"

print(chars.isalpha()) # True

print(chars.isalnum()) # True -> Checks letters/numbers

print(chars.isdigit()) # False

print(chars.isspace()) # False ->  Checks only spaces
