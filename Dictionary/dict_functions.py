student = {
    "id" : 101,
    "name" : "Sidra Fatima",
    "roll" : 1,
    "age": 8,
    "marks" : 9.3,
    "address": "Chauhatta Hajipur, Vaishali (Bihar)"
}

print(student, "\n")

# <<<<<<<<<<<<<<<<< DICTIONARY FUNCTIONS >>>>>>>>>>>>>>>>>>>>

# 1. get method
print(f"Student Id: {student.get("id")}")
print(f"Name: {student.get("name")}")
print(f"Roll: {student.get("roll")}")
print(f"Age: {student.get("age")} years")
print(f"Marks: {student.get("marks")} CGPA")
print(f"Address: {student.get("address")}\n")

# get method with default value
print(f"Contact : {student.get("contact", "Not Found")}\n")

# 2. keys method
print(student.keys()) # return all keys of the dictionary

# 3. values method
print(student.values()) # return all values of the dictionary

# 4. items method
print(student.items()) # return all keys and values in the form of tuple of the dictionary

# 5. update method
print(f"\nAfter updating marks and contact of {student.get('name')}")
student.update({"marks": "9.5 CGPA"}) # Updates existing keys or adds new ones
student.update({"contact": "7480820409"}) # Updates existing keys or adds new ones
print(student)

# 6. pop method
print(student.pop("age")) # Removes a key and returns its value.

