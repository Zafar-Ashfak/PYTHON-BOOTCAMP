# Write a program to find the maximum element in a list using recursion
def getmax(nums, n):
    # Base Case
    if n == 0:
        return nums[0]
    # Recursive Call
    max_element = getmax(nums, n - 1)
    if nums[n - 1] > max_element:
        return nums[n - 1]
    else:
        return max_element

def main():
    print("Program to find the maximum element in a list using recursion")
    nums = [11, 49, 22, 116, 44, 36]
    n = len(nums) - 1
    res = getmax(nums, n)
    print(f"Maximum element in the list is: {res}")

main()