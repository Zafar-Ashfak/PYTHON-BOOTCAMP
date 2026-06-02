# nums = {} # dict

# We can store different types of data in the set
mySet = {2, 5, 8, "Zafar", 4.6, 9.342, True, False, None, '8'} # set

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
set2 = { 3, 4, 8, 10, 12, 15 }

print(f"{set1.union(set2)}\n") # Output -> { 1, 2, 3, 4, 8, 10, 12, 15 }

# 9. intersection method -> Returns common elements.
print(f"{set1.intersection(set2)}\n") # Output -> { 4, 8, 12 }

# 10. difference() method -> Returns elements present in the first set but not the second.
print(f"Difference of set1 and set2 is: {set1.difference(set2)}") # Output -> {1, 2 }
print(f"Difference of set2 and set1 is: {set2.difference(set1)}\n") # Output -> { 3, 10, 15 }

# 11. symmetric_difference() method -> Returns elements that are in either set but not both.
print(f"Symmetric difference of set1 and set2 is: {set1.symmetric_difference(set2)}\n") # Output -> { 1, 2, 3, 10, 15 }

# 12. issubset() method -> Checks if one set is a subset of another
print({1, 4, 8}.issubset(set1)) # True
print({1, 9, 15}.issubset(set2) , "\n") # False

# 13. issuperset() method -> Checks if one set contains another set
print(set1.issuperset({1, 2, 8})) # True
print(set1.issuperset({2, 3, 12, 17}), "\n") # False

# 14. len() method -> returns the length of the set
print(f"Length of the set1 is: {len(set1)}")
print(f"Length of the set2 is: {len(set2)}\n")

# 15. max() method -> returns the max element of the set
print(f"Largest element of the set1 is: {max(set1)}")
print(f"Largest element of the set2 is: {max(set2)}\n")

# 16. min() method -> returns the max element of the set
print(f"Smallest element of the set1 is: {min(set1)}")
print(f"Smallest element of the set2 is: {min(set2)}\n")

# 17. sum() method -> adds each element of the set
print(f"Sum of the elements of the set1 si: {sum(set1)}")
print(f"Sum of the elements of the set2 si: {sum(set2)}\n")


# Removing duplicate elements using set
numbersList = [ 1, 2, 5, 3, 5, 7, 2, 8, 6, 4, 7, 9 ]
print(f"Numbers list: {numbersList}, Type: {type(numbersList)}")
uniqueSet = set(numbersList)
print(f"Numbers set: {uniqueSet}, Type: {type(uniqueSet)}")