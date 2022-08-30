# GROKKING - SUBSETS

# To generate all subsets of the given set, we can use the Breadth First Search approach
# 1. Start with an empty set
# 2. Add the first number to all existing subsets to create new subsets
# 3. Add the second number to all the existing subsets
# 4. Add the third number to all the existing subsets


# SUBSETS
# Given a set with distinct elements, find all of its distinct subsets

def find_subsets(nums):
    # Start with an empty subset
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