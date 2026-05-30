
myList = ["Zafar", 12, 54.67, True, None] # We can store different types of data in python list

print(myList)

fruits = ["apple", "banana", "cherry", "kiwi"]
print(fruits)
# <<<<<<<<<<<<<<<PYTHON LIST FUNCTIONS>>>>>>>>>>>>>>>>>
# 1. append function
fruits.append("mango") # adds an element at the end of the list
print(fruits)


# 2. insert function
fruits.insert(3, "grapes") # adds an element at the given index in the list
print(fruits)

# 3. remove function
fruits.remove("kiwi") # removes and returns the given element
print(fruits)


nums = [1, 4, 7, 2, 9, 3, 8, 5, 6]

# 4. extend function
nums.extend([10, 13, 12, 11]) # adds all elements from another iterable
print(nums)


# 5. index function
print(f" Element 8 is at index: {nums.index(8)}") # returns the index of the given element

# 6. count function
print(f"Element 5 occurs {nums.count(5)} times") # counts and returns the occurrences of the given element

# 7. sort function
nums.sort() # sort the given list in ascending order
print("Sorted list in ascending order")
print(nums)

# 8. reverse function
nums.reverse() # sort the given list in descending order
print("Sorted list in descending order")
print(nums)

# 9. copy function
new_nums = nums.copy() # creates a shallow copy of the list
print(new_nums)

# 10. len function
print(f"Length of the list is: {len(nums)}") # returns the length of the list


# 11. pop function
print(f" Popped value: {nums.pop()}") # removes and returns the last element
print(f" Popped value: {nums.pop(3)}") # removes and returns the element at index 3
print(nums)

# 12. clear function
print(nums.clear()) # removes all elements of the list


# ________________________________________________________________________________

nums = [10, 54, 23, 43, 36, 23, 30]
print(nums)

# 13. max function
print(f"Maximum element in the list is: {max(nums)}") # returns the max element of the list

# 14. min function
print(f"Minimum element in the list is: {min(nums)}") # returns the min element of the list

# 15. sum function
print(f"Sum of the elements in the list is: {sum(nums)}") # add each element of the list

# list slicing
print(nums[1 : 5])
print(nums[ : 4])
print(nums[3 : ])
print(nums[0 : 6 : 2])

# Converting list to tuple
myTuple = tuple(nums)
print("Converting to tuple from list")
print(myTuple)
print(type(myTuple))

