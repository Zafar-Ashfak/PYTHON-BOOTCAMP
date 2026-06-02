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
print(nums)

# 6. clear() method -> Removes all elements
nums.clear()
print(f"{nums}\n") # Output -> set()
