from typing import Optional
from collections import deque

from typing import List


# Definition of binary tree node.
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def find_paths(self, root, path, result):
        if root is None:
            return

        # Add the current node to the current path
        path.append(root.data)

        # If the current node is a leaf node, add the current path to the result
        if root.left is None and root.right is None:
            result.append(path.copy())
        else:
            # Recur for the left and right subtrees
            self.find_paths(root.left, path, result)
            self.find_paths(root.right, path, result)

        # Remove the current node from the current path to backtrack
        path.pop()

    def Paths(self, root: Optional[Node]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        self.find_paths(root, [], result)
        return result
