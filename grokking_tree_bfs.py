# TREE BREADTH FIRST SEARCH

# BINARY TREE LEVEL ORDER TRAVERSAL
# Given a binary tree, populate an array to represent its level-by-level traversal
# Populate the values of all nodes of each level from left to right in separate sub-arrays

from __future__ import print_function
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def traverse1(root):
    result = []

    # Check that there is a root value to start the tree
    if root is None:
        return result

    # Can also be written as queue = []
    # deque is a double-ended queue
    queue = deque()
    # The root node is added to the queue
    queue.append(root)

    # While there are elements in the queue, perform the following
    while queue:
        # The size of the level is the length of the current queue
        levelSize = len(queue)
        # Set an empty array to store the values of the current level
        currentLevel = []

        # Iterate until the current level is empty
        for _ in range(levelSize):
            # Can also be written as queue.pop(0), since you are always taking the first element
            currentNode = queue.popleft()
            # Add the value of the node to the current level
            currentLevel.append(currentNode.val)

            # Insert the children of current node in the queue, first left, then right
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        # After the level has been completed, add the current level array to the result array
        result.append(currentLevel)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse1(root)))

main()

# Time Complexity - O(N)
# Space Complexity - O(N)


###################################################################################################

# REVERSE LEVEL ORDER TRAVERSAL
# Given a binary tree, populate an array to represent its level-by-level traversal in reverse
# order, i.e., the lowest level comes first.

class TreeNode:
    def __init__ (self, val):
        self.val = val
        self.left = None
        self.right = None

def traverse2(root):
    # The final results will be saved in a double ended queue, so we can add the currentLevel
    # values in from the left
    result = deque()

    # Check if the root value exists to start the tree
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        currentLevel = []

        for _ in range(levelSize):
            # Pop the first item in the queue
            currentNode = queue.popleft()
            # Add the node value to the current level array
            currentLevel.append(currentNode.val)

            # Check for children of the current node and add them to the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        # Add teh current level to the left end of the queue
        result.appendleft(currentLevel)

    return list(result)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse2(root)))

main()

# Time Complexity - O(N)
# Space Complexity - O(N)


###################################################################################################

# ZIGZAG TRAVERSAL
# Given a binary tree, populate an array to represent its zigzag level order traversal. Populate
# the values of all nodes of the first level from left to right, then right to left for the next
# level and keep alternating in the smae manner for following levels

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def traverse3(root):
    result = []

    # Check if a tree exists
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    # Set a variable to keep track of direction of each level
    left_to_right = True

    while queue:
        levelSize = len(queue)
        currentLevel = deque()
        for _ in range(levelSize):
            currentNode = queue.popleft()

            # Add the node to the current level based on the traverse direction
            if left_to_right == True:
                currentLevel.append(currentNode.val)
            else:
                currentLevel.appendleft(currentNode.val)

            # Add the children of the current node to the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        result.append(list(currentLevel))

        # Update traverse direction
        if left_to_right == True:
            left_to_right = False
        else:
            left_to_right = True

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse3(root)))

main()

# Time Complexity - O(N)
# Space Complexity - O(N)


###################################################################################################

# LEVEL AVERAGES IN A BINARY TREE
# Given a binary tree, populate an array to represent the averages of all of its levels

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_level_averages(root):
    result = []

    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        # Initialize the levelSize and the levelSum values
        levelSize = len(queue)
        levelSum = 0.0

        for _ in range(levelSize):
            currentNode = queue.popleft()

            # Add the node's value to the running sum of the level
            levelSum += currentNode.val

            # Check for children and add them to the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        # Add the current level's average to the results array
        result.append(levelSum / levelSize)

    return result
            

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))

main()

# Time Complexity - O(N)
# Space Complexity - O(N)


###################################################################################################

# LEVEL MAX VALUE IN A BINARY TREE
# Given a binary tree, find the maximum value on each level

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_level_max(root):
    result = []

    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)
        maxValue = 0

        # Iterate until the current level is empty
        for _ in range(levelSize):
            currentNode = queue.popleft()
            # Compare the current value with current max, and update max value if necessary
            maxValue = max(maxValue, currentNode.val)

            # Insert the children of current node in the queue, first left, then right
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        # After the level has been completed, add the current level array to the result array
        result.append(maxValue)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level max values are: " + str(find_level_max(root)))

main()

# Time Complexity - O(N)
# Space Complexity - O(N)


###################################################################################################

# MINIMUM DEPTH OF A BINARY TREE
# Find the minimum depth of a binary tree - the number of nodes along the shortest path from
# the root node to the nearest leaf node

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_minimum_depth(root):
    if root is None:
        return 0

    queue = deque()
    queue.append(root)
    minimum_tree_depth = 0

    while queue:
        minimum_tree_depth += 1
        levelSize = len(queue)
        
        for _ in range(levelSize):
            currentNode = queue.popleft()

            # Check if the current node is a leaf node
            if not currentNode.left and not currentNode.right:
                return minimum_tree_depth
            
            # Check for children and add them to the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)



def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))

main()

# Time Complexity - O(N)
# Space Complexity - O(N)


###################################################################################################

# MAXIMUM DEPTH OF A BINARY TREE
# Given a binary tree, find it's maximum depth (or height)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_maximum_depth(root):
    
    if root is None:
        return 0

    queue = deque()
    queue.append(root)
    maximum_tree_depth = 0 

    while queue:
        # For each new level in the tree, add one to the max depth value
        maximum_tree_depth += 1
        levelSize = len(queue)
        
        for _ in range(levelSize):
            currentNode = queue.popleft()

            # Check for children and add them to the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

    return maximum_tree_depth


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Maximum Depth: " + str(find_maximum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Maximum Depth: " + str(find_maximum_depth(root)))

main()

# Time Complexity - O(N)
# Space Complexity - O(N)


###################################################################################################

# LEVEL ORDER SUCCESSOR
# Given a binary tree and a node, find the level order successor of the given node in the tree
# The level order successor is the node that appears right after the given node in the level 
# order traversal

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_successor(root, key):
    
    if root is None:
        return None

    queue = deque()
    queue.append(root)

    while queue:
        currentNode = queue.popleft()

        # Check for children and add to the queue
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

        # Break if we find the key
        if currentNode.val == key:
            break

    return queue[0] if queue else None


def main():
  
    root = TreeNode(1);
    root.left = TreeNode(2);
    root.right = TreeNode(3);
    root.left.left = TreeNode(4);
    root.left.right = TreeNode(5);
  
    result = find_successor(root, 3)
    if result:
        print(result.val)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
  
    result = find_successor(root, 9)
    if result:
        print(result.val)
  
    result = find_successor(root, 12)
    if result:
        print(result.val)

main()

# Time Complexity - O(N)
# Space Complexity - O(N)


###################################################################################################

# CONNECT LEVEL ORDER SIBLINGS
# Given a binary tree, connect each node with its level order successor. The last node of each
# level should point to a null node

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # Level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()


def connect_level_order_siblings(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)
    while queue:
        previousNode = None
        levelSize = len(queue)
        # Connect all nodes in each level
        for _ in range(levelSize):
            currentNode = queue.popleft()
            if previousNode:
                previousNode.next = currentNode
            previousNode = currentNode

            # Check for children and add to queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()

main()

# Time Complexity - O(N)
# Space Complexity - O(N)


###################################################################################################

# CHALLENGE 1 : CONNECT ALL LEVEL ORDER SIBLINGS
# Given a binary tree, connect each node with its level order successor. The last node of each
# level should point to the first node of the next level.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


    # Tree traversal using 'next' pointer
    def print_tree(self):

        print("Traversal using 'next' pointer: ", end='')
        current = self

        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def connect_all_siblings(root):

    if root is None:
        return

    queue = deque()
    queue.append(root)
    currentNode = None
    previousNode = None

    while queue:
        currentNode = queue.popleft()
        if previousNode:
            previousNode.next = currentNode
        previousNode = currentNode

        # Check for children of current node and add to queue
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)
    root.print_tree()

main()

# Time Complexity - O(N)
# Space Complexity - O(N)


###################################################################################################

# CHALLENGE 2: RIGHT VIEW OF A BIANRY TREE
# Given a binary tree, return an array containing nodes in its right view. The right view of a
# binary tree is the set of nodes visible when the tree is seen from the right side.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_right_view(root):
    result = []

    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)

        for i in range(levelSize):
            currentNode = queue.popleft()

            if i == levelSize - 1:
                result.append(currentNode)

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')

main()

# Time Complexity - O(N)
# Space Complexity - O(N)