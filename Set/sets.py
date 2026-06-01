# nums = {} # dict

# We can store different types of data in the set
mySet = {1, 2, 5, 8, "Zafar", 4.6, True, None} # set

print(mySet)
print(type(mySet))

uniqueVal = {1 , 3, 5, 7, 3, 6, 8, 5 }
print(uniqueVal) # Output -> {1, 3, 5, 6, 7, 8} prints unique val only

# <<<<<<<<<<<<<<<<<< SET FUNCTIONS >>>>>>>>>>>>>>>>>>

nums = {1, 2, 3, 4, 5}
print(nums)

# 1. add() method -> adds a single element at the end
nums.add(6)
print(nums)

# 2. update() method -> Adds multiple elements from another iterable.
nums.update({7, 8, 9, 10})
print(nums)

