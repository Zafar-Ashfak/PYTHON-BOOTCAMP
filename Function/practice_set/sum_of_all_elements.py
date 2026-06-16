# Write a program to calculate the sum of all the elements in the list

def elements_sum(nums, n):
    # Base Case
    if n == 0:
        return nums[0]

    # Recursive Call
    return nums[n] + elements_sum(nums, n - 1)

def main():
    print("Program to calculate the sum of all the elements in the list")
    nums = [1, 3, 2, 4, 10, 7, 4]
    res = elements_sum(nums, len(nums) - 1)
    print(f"Sum of all the elements in the list is: {res}")

main()
