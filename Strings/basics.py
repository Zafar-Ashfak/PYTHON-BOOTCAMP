from builtins import print

firstName = 'Zafar'

lastName = "Ashfaq"

str = """
Hello I am Md Ashfaq Alam.
I am a software engineer with 1 year of experience.
"""

print(firstName, "" + lastName)
print(str)

#String Slicing

shortStr = str[0 : 15]
print(shortStr)

print(str[ : 10]) # It means print(str[0 : 10])

print(str[0 : ]) # It means print(str[0 : len])

