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

# 1. get() method
print(f"Student Id: {student.get('id')}")
print(f"Name: {student.get('name')}")
print(f"Roll: {student.get('roll')}")
print(f"Age: {student.get('age')} years")
print(f"Marks: {student.get('marks')} CGPA")
print(f"Address: {student.get('address')}\n")

# get() method with default value
print(f"Contact : {student.get('contact', 'Not Found')}\n")

# 2. keys method -> return all keys of the dictionary
print(student.keys())

# 3. values() method -> return all values of the dictionary
print(student.values())

# 4. items() method -> return all keys and values in the form of tuple of the dictionary
print(student.items())

# 5. update() method -> Updates existing keys or adds new ones
print(f"\nAfter updating marks and contact of {student.get('name')}")
student.update({
    "marks": 9.5,
    "contact": 7480820409
})
print(student)

# 6. pop() method -> Removes a key and returns its value
print(f"\nStudent Age: {student.pop('age')}\n")

# 7. popitem() method -> Removes and returns the last inserted key-value pair
print(student.popitem(), "\n")

# 8. copy() method -> Creates a shallow copy of the dictionary
new_student = student.copy()
print("New student details by mistake deleted from database\n", new_student)

# 9. setdefault() method -> Returns the value of a key. If the key doesn't exist, inserts it with a default value.
student.setdefault("age", 10)
print("\n", student)

# 10. clear() method -> clears the dictionary data
# print(student.clear())

# 11. len() method
print(f"\nLength of the student dictionary is: {len(student)}")