# GROKKING - SUBSETS

# SUBSETS
# Given a set with distinct elements, find all of its distinct subsets

# To generate all subsets of the given set, we can use the Breadth First Search approach
# 1. Start with an empty set
# 2. Add the first number to all existing subsets to create new subsets
# 3. Add the second number to all the existing subsets
# 4. Add the third number to all the existing subsets

def find_subsets(nums):
    # Initiate the subset
    subsets = []

    # Start by adding the empty subset
    subsets.append([])

    # Cycle through all the numbers in the provided list
    for currentNumber in nums:
        # Keep track of the total number of subsets
        n = len(subsets)
        # Cycle through all existing subsets and insert the current number
        # in them to create new subsets
        for i in range(n):
            # Pull a subset from the list of subsets
            set1 = list(subsets[i])
            # Add the current number to subset to create a new subset
            set1.append(currentNumber)
            # Add the new subset to the list of all subsets
            subsets.append(set1)
  
    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))

main()

# Time Complexity - O(N*(2^N)
# Space Complexity - O(N*(2^N))


###########################################################################################

# SUBSETS WITH DUPLICATES
# Given a set of numbers that might contain duplicates find all of its distinct subsets

# 1. Sort all numbers of the given set, so all duplicates are next to each other
# 2. Follow the same BFS approach as above, but when we have a duplicate, only add it
# to the new subsets that were created in the previous step

def find_subsets_d(nums):
    # Sort the numbers first to handle duplicates
    list.sort(nums)
    # Initiate the subset
    subsets = []
    # Start by adding an empty subset
    subsets.append([])
    # Keep track of start and end indices
    start_index = 0
    end_index = 0

    # Cycle through all nums values
    for i in range(len(nums)):
        start_index = 0
        # If current element is the same as the previous element, create new subsets 
        # from only the subsets that were created in the previous step
        if i > 0 and nums[i] == nums[i - 1]:
            start_index = end_index + 1
        end_index = len(subsets) - 1

        # Cycle through the list of subsets from start position to end position 
        for j in range(start_index, end_index + 1):
            # Pull a subset from the list of subsets
            set1 = list(subsets[j])
            # Add the current number to subset to create a new subset
            set1.append(nums[i])
            # Add the new subset to the list of all subsets
            subsets.append(set1)

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets_d([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets_d([1, 5, 3, 3])))

main()

# Time Complexity - O(N*(2^N)
# Space Complexity - O(N*(2^N))


###########################################################################################
