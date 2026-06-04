numsSet = {1, 5, 10, -13, -93, True, False, "Python", "RAG", None}

i = 0

# Since sets aren't indexed, we need to
# convert the set to a list or tuple first
numList = list(numsSet)

# Print set's elements using while loop
while i < len(numList):
    print(numList[i], end=" ")
    i += 1

print("\n")

# Print set's elements using for loop
for e in numList:
    print(e, end=" ")
