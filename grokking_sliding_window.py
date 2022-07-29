# GROKKING - SLIDING WINDOW PROBLEMS

# SLIDING WINDOW ALGORITHM
def find_averages_of_subarrays(K, arr):
    result = []
    windowSum = 0.0
    windowStart = 0

    for windowEnd in range(0, len(arr)):
        windowSum += arr[windowEnd] 
        # When we hit the required window size, K, start sliding the window
        if windowEnd >= K - 1:
            result.append(windowSum / K) # Calculate the average and add it to results
            windowSum -= arr[windowStart] # Subtract the first element 
            windowStart += 1 # Slide the window to the right

    return result


def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))

main()


#######################################################################################

# MAXIMUM SUM SUBARRAY OF SIZE K
def max_sub_array_of_size_k(K, arr):
    max_sum = 0
    windowSum = 0
    windowStart = 0

    for windowEnd in range(0, len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= K - 1:
            max_sum = max(max_sum, windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1
    
    return max_sum

def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))) 
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()

# Time Complexity = O(N)
# Space Complexity = O(1)


#######################################################################################

# SMALLEST SUBARRAY WITH A GREATER SUM

def smallest_subarray_sum(s, arr):
    min_length = len(arr) + 1
    windowSum = 0
    windowStart = 0

    for windowEnd in range(0, len(arr)):
        windowSum += arr[windowEnd]
        # Continue growing window until we reach a sum greater than or equal to the target "s"
        while windowSum >= s:
            min_length = min(min_length, windowEnd - windowStart + 1)
            windowSum -= arr[windowStart]
            windowStart += 1
    
    if min_length == len(arr) + 1:
        return 0
    else:
        return min_length

def main():
    print("Smallest subarry length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(8, [2, 2, 1, 1, 1, 1])))

main()

# Time Complexity = O(N)
# Space Complexity = O(1)


#######################################################################################

# LONGEST SUBSTRING WITH MAXIMUM K DISTINCT CHARACTERS
def longest_substring_with_k_distinct(str1, K):
    windowStart = 0
    max_length = 0
    char_frequency = {}

    # Extend the range of the window until we reach a non-distinct character
    for windowEnd in range(0, len(str1)):
        right_char = str1[windowEnd]
        # Add new elements to the hashmap/update values of elements in hashmap
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # If we hit more than K distinct characters, begin shrinking window
        while len(char_frequency) > K:
            left_char = str1[windowStart]
            char_frequency[left_char] -= 1
            # If char_frequency is zero, remove it from the hashmap
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            windowStart += 1
        max_length = max(max_length, windowEnd - windowStart + 1)
    return max_length

def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))

main()

# Time Complexity = O(N)
# Space Complexity = O(K)


#####################################################################################

# FRUITS INTO BASKETS
def fruits_into_baskets(fruits, max_fruit_types):
    windowStart = 0
    max_length = 0
    fruit_frequency = {}

    for windowEnd in range(len(fruits)):
        right_fruit = fruits[windowEnd]
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1

        while len(fruit_frequency) > max_fruit_types:
            left_fruit = fruits[windowStart]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            windowStart += 1
        max_length = max(max_length, windowEnd - windowStart + 1)
    return max_length

def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'], 2)))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'], 2)))

main()

# Time Complexity = O(N)
# Space Complexity = O(1)


######################################################################################

# LONGEST SUBSTRING WITH DISTINCT CHARACTERS
def non_repeat_substring(str1):
    windowStart = 0 
    max_length = 0 
    char_map = {}

    # Extend range of substring
    for windowEnd in range(len(str1)):
        right_char = str1[windowEnd]
        # if the map already contains 'right_char', then shrink the window from the start
        if right_char in char_map:
            windowStart = max(windowStart, char_map[right_char] + 1)
        # if the map doesn't contain 'right_char, then add it to the char_map
        char_map[right_char] = windowEnd
        # Keep track of the maximum length
        max_length = max(max_length, windowEnd - windowStart + 1)

    return max_length

def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))

main()

# Time Complexity = O(N)
# Space Complexity = O(K)

######################################################################################

# LONGEST SUBSTRING WITH SAME LETTERS AFTER REPLACEMENT
# Given a string with lowercase letters only, if you are allowed to replace no more
# than k letters with any letter, find the length of the longest substring having the
# same letters after replacement

def length_of_longest_substring(str1, k):
    window_start = 0
    max_length = 0
    max_repeat_letter_count = 0
    frequency_map = {}

    # Try to extend the range of the window
    for window_end in range(0, len(str1)):
        right_char = str1[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1

        # Keep track of the max repeating letter count, updating with each character added
        # to the dictionary
        max_repeat_letter_count = max(max_repeat_letter_count, frequency_map[right_char])

        # If the remaining letter count is larger than the number we can replace (k)...
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            # Begin shrinking the window from the start, until we are equal to "k"
            left_char = str1[window_start]
            frequency_map[left_char] -= 1
            window_start += 1

        # Determine the max length after we reached an acceptable range
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def main():
    print("Length of the longest substring with k replaced characters: " + str(length_of_longest_substring("aabccbb", 2)))
    print("Length of the longest substring with k replaced characters: " + str(length_of_longest_substring("abbcb", 1)))
    print("Length of the longest substring with k replaced characters: " + str(length_of_longest_substring("abccde", 1)))

main()

# Time Complexity = O(N)
# Space Complexity = O(1)

######################################################################################

# LONGEST SUBARRAY WITH ONES AFTER REPLACEMENT
# Given an array containing 0s and 1s, if you are allowed to replace no more than 
# 'k' 0s and 1s, find the length of the longest contiguous subarray having all 1s

def length_of_longest_substring(arr, k):
    window_start = 0
    max_length = 0
    max_ones_count = 0

    # Try to extend the range of the window
    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones_count += 1

        # If the remaining 0s count is larger than the number we can replace (k)...
        if (window_end - window_start + 1 - max_ones_count) > k:
            # Begin shrinking the window from the start, until we are equal to "k"
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def main():
    print("Length of the longest substring of 1s: " + str(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2)))
    print("Length of the longest substring of 1s: " + str(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3)))

main()

# Time Complexity = O(N)
# Space Complexity = O(1)


######################################################################################

# CHALLENGE 1 : PERMUTATION IN A STRING
# Given a string and a pattern, find out if the string contains any permutation of the pattern

def find_permutation(str1, pattern):
    window_start = 0
    matched = 0
    char_frequency = {}

    # Add each character in the pattern to a hashmap, tracking the frequency
    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    # Next we will try to match all the characters from the hashmap with the 
    # current window of the string, extending the range as we go
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        # If we match a character from the hashmap, remove 1 from it's frequency
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            # If we've used all of a specific character from the hashmap
            # Add one to the matched value
            if char_frequency[right_char] == 0:
                matched += 1

        # When our matched value is equal to the total items in our hashmap
        # then we have successfully utilized all pattern characters within a 
        # window of the string - the string contains a permutation of the pattern
        if matched == len(char_frequency):
            return True

        # Shrink the winodw by one character at a time - if we don't find a permutation
        # remove characters from left, "sliding" the window to the right and continue checking
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return False



def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))

main()

# Time Complexity = O(N+M)
# Space Complexity = O(M)


######################################################################################

# CHALLENGE 2 : STRING ANAGRAMS
# Given a string and a pattern, find all anagrams of the pattern in the given string
# Similar to challenge 1, but this time we want to return the starting indices of the anagrams

def find_string_anagrams(str1, pattern):
    window_start = 0
    matched = 0
    char_frequency = {}

    # Add all characters from the pattern to a hashmap with their frequency
    for chr in pattern:
        # If the character is not in the hashmap, add it
        if chr not in char_frequency:
            char_frequency[chr] = 0
        # If the character is in the hashmap, add one to the frequency value
        char_frequency[chr] += 1
    
    result_indices = []
    # Next we will try to match all the characters from the hashmap with the 
    # current window of the string, extending the range as we go
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        # If we match a character from the hashmap, remove 1 from it's frequency
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            # If we've used all of a specific character from the hashmap
            # Add one to the matched value
            if char_frequency[right_char] == 0:
                matched += 1

        # If we find a permutation of the pattern in the string, add the starting 
        # point index (window_start) to the results array
        if matched == len(char_frequency):
            result_indices.append(window_start)

        # Shift sliding window - shrinking from the left
        # Remove starting character from "matched" and add back to unused characters in hashmap
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return result_indices


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))

main()

# Time Complexity = O(N+M)
# Space Complexity = O(M)

######################################################################################

# CHALLENGE 3 : SMALLEST WINDOW CONTAINING SUBSTRING
# Given a string and its pattern, find the smallest substring in the given string which
# has all the character occurences of the given pattern

def find_substring(str1, pattern):
    window_start = 0
    matched = 0 
    substr_start = 0
    min_length = len(str1) + 1
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1
    
    # Try to extend the range of the window
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0:
                matched += 1

        # Shrink the window if possible
        while matched == len(pattern):
            if min_length > (window_end - window_start + 1):
                min_length = window_end - window_start + 1
                substr_start = window_start
            
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    
    if min_length > len(str1):
        return ""
    return str1[substr_start:substr_start + min_length]


def main():
    print(find_substring("aabdec", "abc"))
    print(find_substring("aabdec", "abac"))
    print(find_substring("abdbca", "abc"))
    print(find_substring("adcad", "abc"))

main()

# Time Complexity = O(N+M)
# Space Complexity = O(M)


######################################################################################

# CHALLENGE 4 : WORDS CONCATENATION
# Given a string and a list of words, find all the starting indices of substrings in the
# given string that are a concatenation of all the given words exactly once wihtout any
# overlapping of words

# STEPS:
# 1. Keep the frequency of every word in the hashmap
# 2. Starting from every index of the string, try to match all the words
# 3. In each iteration, keep track of all the words that we have already seen in another hashmap
# 4. If a word is not found or has a higher frequency than required, move to next character in string
# 5. Store the index if we have found all the words

def find_word_concatenation(str1, words):
    if len(words) == 0 or len(words[0]) == 0:
        return []
    
    word_frequency = {}

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    result_indices = []
    word_count = len(words)
    word_length = len(words[0])

    for i in range((len(str1) - word_count * word_length) + 1):
        words_seen = {}
        for j in range(0, word_count):
            next_word_index = i + j * word_length
            # Get the next word from the string
            word = str1[next_word_index: next_word_index + word_length]
            # If we don't need this word, break
            if word not in word_frequency:
                break

            # Add the word to the "words_seen" hashmap
            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            # If the word has a higher frequency than required, break
            if words_seen[word] > word_frequency.get(word, 0):
                break
            
            # If we find all words, store the index
            if j + 1 == word_count:
                result_indices.append(i)

    return result_indices


def main():
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
    print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))

main()

# Time Complexity = O(N*M)
# Space Complexity = O(N+M)

