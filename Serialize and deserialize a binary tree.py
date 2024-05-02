class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to serialize a tree and return a list containing nodes of the tree.
    def serialize(self, root):
        def dfs(node):
            if not node:
                return ['None']
            serialized = [str(node.data)]
            serialized.extend(dfs(node.left))
            serialized.extend(dfs(node.right))
            return serialized
        
        return dfs(root)

    # Function to deserialize a list and construct the tree.
    def deSerialize(self, a):
        def dfs():
            val = next(vals)
            if val == 'None':
                return None
            node = Node(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        
        vals = iter(a)
        return dfs()
