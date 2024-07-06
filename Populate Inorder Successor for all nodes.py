class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None

class Solution:
    def populateNext(self, root):
        self.prev = None  # Track the previous node in reverse inorder
        
        def populateNextUtil(node):
            if node:
                # Recur on the right subtree
                populateNextUtil(node.right)
                
                # Set the next pointer of the current node
                node.next = self.prev
                
                # Update prev to current node
                self.prev = node
                
                # Recur on the left subtree
                populateNextUtil(node.left)
        
        # Start the recursive traversal
        populateNextUtil(root)
