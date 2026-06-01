# nums = {} # dict

# We can store different types of data in the set
mySet = {1, 2, 5, 8, "Zafar", 4.6, True, None} # set

print(mySet)
print(f"{type(mySet)}\n")

uniqueVal = {1 , 3, 5, 7, 3, 6, 8, 5 }
print(f"Set stores unique value only\n{uniqueVal}\n") # Output -> {1, 3, 5, 6, 7, 8} prints unique val only

# <<<<<<<<<<<<<<<<<< SET FUNCTIONS >>>>>>>>>>>>>>>>>>

nums = {1, 2, 3, 4, 5}
print(f"Original set: {nums}\n")

# 1. add() method -> adds a single element at the end
nums.add(6)
print(f"After adding 6 in the nums set: {nums}\n")

# 2. update() method -> Adds multiple elements from another iterable.
nums.update({7, 8, 9, 10})
print(f"After adding multiple elements: {nums}\n")

# 3. remove() method -> removes an element
nums.remove(5)
print(f"After removing 5 from the set: {nums}\n")
