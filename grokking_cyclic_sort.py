# GROKKING - CYCLIC SORT

# CYCLIC SORT
# Given an array containing n objects. Each object, when created, was assigned a unique number
# from the range 1 to n based on their creation sequence. Write a function to sort the objects
# in-place on their creation sequence number.

from re import L


def cyclic_sort(nums):
    i = 0

    # Cycle through the entire list of numbers
    while i < len(nums):
        j = nums[i] - 1

        # If the values are different...
        if nums[i] != nums[j]:
            # ...Swap locations in the array...
            nums[i], nums[j] = nums[j], nums[i]
        # ...until the array indices are the same, then move to the next i in the cycle
        else:
            i += 1
    
    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))

main()

# Time Complexity - O(n)
# Space Complexity - O(1)


################################################################################################

# FIND THE MISSING NUMBER
# Given an array containing n distinct numbers taken from the range 0 to n. Since the array 
# has only n numbers out of the total "n+1" numbers, find the missing number

def find_missing_number(nums):
    i = 0
    n = len(nums)

    while i < n:
        j = nums[i]

        # if the value is less than the length of array and not equal...
        if nums[i] < n and nums[i] != nums[j]:
            # ...swap locations in the array
            nums[i], nums[j] = nums[j], nums[i]
        # otherwise, go to the next step in the cycle
        else:
            i += 1

    # Once the list has been sorted, check that all values match their index
    # If a number is missing from it's index, return the value
    for i in range(0, n):
        if nums[i] != i:
            return i

    # If no values are missing, return the lenngth of the array
    return n


def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))

main()

# Time Complexity - O(n)
# Space Complexity - O(1)


################################################################################################
        


