# GROKKING - CYCLIC SORT

# CYCLIC SORT
# Given an array containing n objects. Each object, when created, was assigned a unique number
# from the range 1 to n based on their creation sequence. Write a function to sort the objects
# in-place on their creation sequence number.

def cyclic_sort(nums):
    i = 0

    # Cycle through the entire list of numbers
    while i < len(nums):
        j = nums[i] - 1

        # Continue swapping values until...
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        # ...the array indices are the same, then move to the next i in the cycle
        else:
            i += 1
    
    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))

main()



################################################################################################