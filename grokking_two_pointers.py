# GROKKING - TWO POINTER PROBLEMS

# PAIR WITH TARGET SUM (TWO POINTER ALGORITHM)
# Given an array of sorted numbers and a target sum, find a pair in the array whose
# sum is equal to the given target

def pair_with_target_sum(arr, target_sum):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return[left, right]

        if target_sum > current_sum:
            # we need a larger sum - move up the left index
            left += 1
        else:
            # we need a smaller sum - move down the right index
            right -= 1
    return None

def main():
  print("Pair with target sum: " + str(pair_with_target_sum([1, 2, 3, 4, 6], 6)))
  print("Pair with target sum: " + str(pair_with_target_sum([2, 5, 9, 11], 11)))

main()

# Time Complexity - O(N)
# Space Complexity - O(1)


###########################################################################################

# REMOVE DUPLICATES
# Given an array of sorted numbers, remove all duplicate number instances from it in-place,
# such that each element appears only once

def remove_duplicates(arr):
    # index of the next non-duplicate element
    next_non_duplicate = 1
    i = 0

    while i < len(arr):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1

    return next_non_duplicate


def main():
  print("Array new length: " + str(remove_duplicates([2, 3, 3, 3, 6, 9, 9])))
  print("Array new length: " + str(remove_duplicates([2, 2, 2, 11])))

main()

# Time Complexity - O(N)
# Space Complexity - O(1)


############################################################################################

# SQUARING A SORTED ARRAY (WITH NEGATIVE VALUE INPUTS)
# Given a sorted array, created a new array containing squares of all the numbers of the
# input array in the sorted order

def make_squares(arr):
    length = len(arr)

    squares = [0 for x in range(length)]

    highestSquareIndex = length - 1
    left = 0
    right = length - 1

    while left <= right:
        # Calculate the squares of the leftmost and rightmost items in the array
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]

        # If the left value is larger, add it to the rightmost index position of the results
        # And shift to the right to the next most left position
        if leftSquare > rightSquare:
            squares[highestSquareIndex] = leftSquare
            left += 1
        # If the right value is larger, add it to the rightmost index position of the results
        # And shift to the left to the next most right position
        else:
            squares[highestSquareIndex] = rightSquare
            right -= 1
        # Update the highest square index to the next highest position in the results array
        highestSquareIndex -= 1
    
    return squares


def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))

main()

# Time Complexity - O(N)
# Space Complexity - O(N)


############################################################################################

# TRIPLET SUM TO ZERO
# Given an array of unsorted numbers, find all unique triplets in it that add up to zero

def search_triplets(arr):
    # Initiate array to store results
    triplets = []
    # Sort the array provided
    arr.sort()

    for i in range(0, len(arr)-1):
        left = i + 1
        right = len(arr) - 1
        while left <= right:
            # Add values to determine current sum
            currentSum = arr[i] + arr[left] + arr[right]
            # If a solution is found, add it to the results array
            if currentSum == 0:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            # If the sum is less than 0, move the leftmost value up to try larger value
            elif currentSum < 0:
                left += 1
            # If the sume is greater than 0, move the rightmost value down to try smaller value
            elif currentSum > 0:
                right -= 1

    return triplets

def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))

main()

# Time Complexity - O(N^2) Approximately 
# O(N) for loop + O(N*logN) sorting array = O(N^2) 
# Space Complexity - O(N)


############################################################################################

# TRIPLET SUM CLOSE TO TARGET
# Given an array of unsorted numbers and a target number, find a triplet in the array whose
# sum is as close to the target number as possible, return the sum of the triplet

def triplet_sum_close_to_target(arr, target_sum):
    # Sort the array provided 
    arr.sort()
    smallest_difference = float("inf")

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while (left < right):
            target_diff = target_sum - arr[i] - arr[left] - arr[right]
            # If the target_diff is zero, we've found a triple that is equal to the target sum
            if target_diff == 0:
                return target_sum

            # Handle smallest sum when there is more than one solutin
            if (abs(target_diff) < abs(smallest_difference)) or ((abs(target_diff) == abs(smallest_difference)) and (target_diff > smallest_difference)):
                # Save the closest difference
                smallest_difference = target_diff

            # We need a triplet with a larger sum
            if target_diff > 0:
                left += 1
            # We need a triplet with a smaller sum
            else:
                right -= 1
    
    return target_sum - smallest_difference


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))

main()

# Time Complexity - O(N^2) Approximately 
# Space Complexity - O(N)


############################################################################################

# TRIPLETS WITH SMALLER SUM
# Given an array of unsorted numbers and a target sum, count all triplets in it such that
# arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices

def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        count += search_pair(arr, target - arr[i], i)
    return count


def search_pair(arr, target_sum, first):
    count = 0
    left = first + 1
    right = len(arr) - 1
    while (left < right):
        if arr[left] + arr[right] < target_sum:
            count += right - left
            left += 1
        else:
            right -= 1
    
    return count


def main():
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))

main()

# Time Complexity - O(N^2) Approximately 
# Space Complexity - O(N)


############################################################################################

# SUBARRAYS WITH PRODUCTS LESS THAN A TARGET
# Given an array with positive numbers and a positive target number, find all of its
# contiguous subarrays whose product is less than the target number

from collections import deque

def find_subarrays(arr, target):
    result = []
    product = 1
    left = 0 

    for right in range(len(arr)):
        product *= arr[right]
        
        while (product >= target and left <= right):
            product /= arr[left]
            left += 1
        temp_list = deque()
        
        for i in range(right, left-1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))
    
    return result


def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 6, 5], 50))

main()

# Time Complexity - O(N^3) Approximately 
# O(N) for loop + O(N^2) creating subarrays = O(N^3) 
# Space Complexity - O(N)


############################################################################################