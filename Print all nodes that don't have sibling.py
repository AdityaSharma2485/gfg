def noSibling(root):
    result = []

    # Depth-first traversal function to count children and find nodes without siblings
    def dfs(node, parent):
        if not node:
            return
        
        # If the current node is a leaf node (no children), return
        if not node.left and not node.right:
            return
        
        # If the current node has only one child, add its value to the result list
        if not node.left:
            result.append(node.right.data)
        elif not node.right:
            result.append(node.left.data)
        
        # Recursively traverse the left and right subtrees
        dfs(node.left, node)
        dfs(node.right, node)
    
    # Start the depth-first traversal from the root
    dfs(root, None)
    
    # Sort the result list in increasing order
    result.sort()
    
    # Return the result list or -1 if all nodes have siblings
    return result if result else [-1]
