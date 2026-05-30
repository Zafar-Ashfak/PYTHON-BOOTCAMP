myTuple = (34, 58.13, 'A', "Computer", True, None) # We can store different types of data in the tuple

print(myTuple)
print(type(myTuple))

nums = (11, 36, 21, 54, 38, 29, 42, 45, 21, 67, 86, 16, 50, 71)

# <<<<<<<<<<<<<<< TUPLE METHODS >>>>>>>>>>>>>>>>>>>

print(f"Length of the tuple is: {len(nums)}")

print(f"Element 21 occurs {nums.count(21)} times in the given list") # Counts the occurrences of an element.

print(f"Element 42 is at index: {nums.index(42)}") # Returns the index of the first occurrence of an element.

print(f"Maximum element is {max(nums)} in the given tuple") # Returns the max element from the tuple

print(f"Minimum element is {min(nums)} in the given tuple") # Returns the min element from the tuple

print(f"Sum of the elements in the tuple is: {sum(nums)}") # Adds the elements in the tuple

print("\nSorted tuple")
print(sorted(nums)) # sort the elements in the ascending order

# Slicing
print("Tuple Slicing")
print(nums[0 : 7])
print(nums[3 : ])
print(nums[ : 6])
print(nums[0 : 10 : 3])

# Converting tuple to list
myList = list(nums)

print("Converting to list from tuple")
print(myList)
print(type(myList))