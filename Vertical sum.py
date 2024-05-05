class Solution:
    def verticalSum(self, root):
        if not root:
            return []

        # Initialize a dictionary to store the vertical sums
        vertical_sums = {}

        # Helper function to perform vertical traversal and update vertical sums
        def traverse(node, col):
            if not node:
                return
            # Update vertical sum for the current column
            vertical_sums[col] = vertical_sums.get(col, 0) + node.data
            # Recursively traverse left and right subtrees
            traverse(node.left, col - 1)
            traverse(node.right, col + 1)

        # Start vertical traversal from the root node
        traverse(root, 0)

        # Extract the vertical sums from the dictionary and return as a list
        return [vertical_sums[col] for col in sorted(vertical_sums)]
        
