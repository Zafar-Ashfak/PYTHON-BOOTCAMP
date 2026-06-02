# nums = {} # dict

# We can store different types of data in the set
mySet = {2, 5, 8, "Zafar", 4.6, 9.342, True, False, None} # set

print(mySet)
print(f"{type(mySet)}\n")

uniqueVal = {1 , 3, 5, 7, 3, 6, 8, 5 }
# Output -> {1, 3, 5, 6, 7, 8} Prints unique val only & Duplicate values are automatically removed.
print(f"Set stores unique value only\n{uniqueVal}\n")

# <<<<<<<<<<<<<<<<<< SET FUNCTIONS >>>>>>>>>>>>>>>>>>

nums = {1, 2, 3, 4, 5}
print(f"Original set: {nums}\n")

# 1. add() method -> adds a single element to the set
nums.add(6)
print(f"After adding 6 in the nums set: {nums}\n")

# 2. update() method -> Adds multiple elements from another iterable.
nums.update({7, 8, 9, 10})
print(f"After adding multiple elements: {nums}\n")

# 3. remove() method -> # removes an element from the set; raises KeyError if not found
nums.remove(5)
print(f"After removing 5 from the set: {nums}\n")

# 4. discard() method -> removes an element if present in the set
nums.discard(17)
print(f"After discarding 17 from the set: {nums}\n")

# 5. pop() method -> Removes and returns a random element.
print(f"Popped value: {nums.pop()}\n")
print(f"After popping the random element: {nums}")

# 6. copy() method -> Creates a shallow copy of the set
new_nums = nums.copy()
print(f"Copied set: {new_nums}\n")


# 7. clear() method -> Removes all elements
nums.clear()
print(f"{nums}\n") # Output -> set()

# 8. union() method ->  Combines two sets and returns all unique elements from both sets
set1 = { 1, 2, 4, 8, 12 }
set2 = { 1, 3, 6, 8, 12, 15}

print(f"{set1.union(set2)}\n") # Output -> { 1, 2, 3, 4, 6, 8, 12, 15 }

# 9. intersection method -> Returns common elements.
print(f"{set1.intersection(set2)}\n") # Output -> { 1, 8, 12 }

# 10. difference() method -> Returns elements present in the first set but not the second.
print(f"Difference of set1 and set2 is: {set1.difference(set2)}") # Output -> { 2, 4 }
print(f"Difference of set2 and set1 is: {set2.difference(set1)}") # Output -> { 3, 6, 15 }
