myTuple = (34, 58.13, 'A', "Computer", True, None) # We can store different types of data in the tuple

print(myTuple)
print(type(myTuple))

nums = (11, 16, 21, 54, 38, 29, 42, 45, 21, 67, 86, 62, 50, 71)

# <<<<<<<<<<<<<<< TUPLE METHODS >>>>>>>>>>>>>>>>>>>

print(f"Length of the tuple is: {len(nums)}")

print(f"Element 21 occurs {nums.count(21)} times in the given list") # Counts the occurrences of an element.

print(f"Element 42 is at index: {nums.index(42)}") # Returns the index of the first occurrence of an element.

print(f"Maximum element is {max(nums)} in the given tuple") # Returns the max element from the tuple

print(f"Minimum element is {min(nums)} in the given tuple") # Returns the min element from the tuple

