student = {
    "id" : "101",
    "name" : "Sidra Fatima",
    "roll" : "01",
    "marks" : "9.3 CGPA",
    "address": "Chauhatta Hajipur, Vaishali (Bihar)"
}

print(student)

# <<<<<<<<<<<<<<<<< DICTIONARY FUNCTIONS >>>>>>>>>>>>>>>>>>>>

print(f"Student Id: {student.get("id")}")
print(f"Name: {student.get("name")}")
print(f"Roll: {student.get("roll")}")
print(f"Marks: {student.get("marks")}")
print(f"Address: {student.get("address")}")

print(f"Contact : {student.get("contact", "Not Found")}")

print(student.keys())
print(student.values())
print(student.items())