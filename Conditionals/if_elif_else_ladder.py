age = int(input("Enter your age: "))

if age < 0:
    print("You entered an invalid age")
elif 0 <= age < 2:
    print("You are an infant")
elif 2 <= age < 4:
    print("You are a toddler")
elif 4 <= age < 13:
    print("You are a child")
elif 13 <= age < 18:
    print("You are a teenager")
elif 18 <= age < 39:
    print("You are an adult")
elif 39 <= age < 59:
    print("You are a middle age person")
else:
    print("You are a senior citizen")
