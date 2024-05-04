class Solution:
    def buildTree(self, inorder, postorder, n):
        if not inorder or not postorder or n == 0:
            return None
        
        # Find the root node
        root_val = postorder[n - 1]
        root_index = inorder.index(root_val)
        root = Node(root_val)
        
        # Recursively build left and right subtrees
        root.right = self.buildTree(inorder[root_index + 1:], postorder[root_index:], n - root_index - 1)
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index], root_index)
        
        return root

    def preorderTraversal(self, root):
        if not root:
            return []
        return [root.data] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

