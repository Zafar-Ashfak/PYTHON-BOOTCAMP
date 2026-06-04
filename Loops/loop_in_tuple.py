myTuple = (-1, -5, 0, 2, 6, 1345, "Python", "Django", "Spring Boot", True, False, None)

# Print tuple's elements using while loop
i = 0
while i < len(myTuple):
    print(myTuple[i], end=" ")
    i += 1

print("\n")

# Print tuple's elements using for loop
for e in myTuple:
    print(e, end=" ")