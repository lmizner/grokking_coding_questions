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
        
# FIND ALL MISSING NUMBERS
# Given an unsorted array containing numbers taken from the range 1 to 'n'. The array can have 
# duplicates, which means some numbers will be missing. Find all those missing numbers.

def find_missing_numbers(nums):
    i = 0

    while i < len(nums):
        j = nums[i] - 1

        # If the values are different...
        if nums[i] != nums[j]:
            # ...Swap locations in the array...
            nums[i], nums[j] = nums[j], nums[i]
        # ...until the array indices are the same, then move to the next i in the cycle
        else:
            i += 1
    
    missing_numbers = []

    # Once te list is sorted, cycle through and add all missing values to an array
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing_numbers.append(i + 1)

    return missing_numbers


def main():
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers([2, 4, 1, 2]))
    print(find_missing_numbers([2, 3, 2, 1]))

main()

# Time Complexity - O(n)
# Space Complexity - O(1)


################################################################################################

# FIND THE DUPLICATE NUMBER
# Given an unsorted array containing 'n+1' numbers taken from the range 1 to 'n'. The array 
# has only one duplicate but it can be repeated multiple time. Find that duplicate number without
# using any extra space - modify the input array.

def find_duplicate(nums):
    i = 0

    while i < len(nums):
        # If the value is not equal to its corresponding index
        if nums[i] != i + 1:
            j = nums[i] - 1

            # If the values are different...
            if nums[i] != nums[j]:
                # ...Swap locations in the array...
                nums[i], nums[j] = nums[j], nums[i]
            # ...otherwise, we've found the duplicate
            else:
                return nums[i]
        
        # When the value is equal to the index, move to the next step in the cycle
        else:
            i += 1
    
    # If there are no duplicate values, return -1
    return -1 


def main():
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 4, 1, 4, 4]))

main()

# Time Complexity - O(n)
# Space Complexity - O(1)

################################################################################################

# FIND ALL DUPLICATE NUMBERS 
# Given an unsorted array containing 'n' numbers taken from the range 1 to n. The array has 
# some numbers appearing twice, find all these duplicate numbers using constant space.

def find_all_duplicates(nums):
    i = 0

    while i < len(nums):
        j = nums[i] - 1

        # If the values are different...
        if nums[i] != nums[j]:
            # ...Swap locations in the array...
            nums[i], nums[j] = nums[j], nums[i]
        # ...until the array indices are the same, then move to the next i in the cycle
        else:
            i += 1

    duplicate_numbers = []

    # Once te list is sorted, cycle through and add all duplicate values to an array
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicate_numbers.append(nums[i])

    return duplicate_numbers


def main():
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))

main()

# Time Complexity - O(n)
# Space Complexity - O(1)


################################################################################################

# CHALLENGE 1: FIND THE CORRUPT PAIR
# Given an unsorted array containing 'n' numbers taken from the range 1 to 'n'. The array
# originally contained all the numbers from 1 to 'n', but due to a data error, one of the 
# numbers got duplicated which also resulted in one number going missing. Find both these numbers.

def find_corrupt_numbers(nums):
    i = 0

    while i < len(nums):
        j = nums[i] - 1

        # If the values are different...
        if nums[i] != nums[j]:
            # ...Swap locations in the array...
            nums[i], nums[j] = nums[j], nums[i]
        # ...until the array indices are the same, then move to the next i in the cycle
        else:
            i += 1

    # Once te list is sorted, cycle through and return corrupt values
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i + 1]

    # If there are no corrupt values, return [-1, -1]
    return [-1, -1]


def main():
    print(find_corrupt_numbers([3, 1, 2, 5, 2]))
    print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))

main()    

# Time Complexity - O(n)
# Space Complexity - O(1)


################################################################################################

# CHALLENGE 2: FIND THE SMALLEST MISSING POSITIVE NUMBER
# Given an unsorted array containing numbers, find the smallest missing positive number in it

def find_first_smallest_missing_positive(nums):
    i = 0
    n = len(nums)

    while i < n:
        j = nums[i] - 1
        
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            # Swap locations in the array...
            nums[i], nums[j] = nums[j], nums[i]
        # ...then move to the next i in the cycle
        else:
            i += 1

    # Once the list is sorted, iterate through the array and return the first index
    # that does not have the correct number
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # Otherwise, return the length of the array plus 1
    return len(nums) + 1


def main():
    print(find_first_smallest_missing_positive([-3, 1, 5, 4, 2]))
    print(find_first_smallest_missing_positive([3, -2, 0, 1, 2]))
    print(find_first_smallest_missing_positive([3, 2, 5, 1]))

main()    

# Time Complexity - O(n)
# Space Complexity - O(1)


################################################################################################


