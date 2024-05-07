def reverseLevelOrder(root):
    if not root:
        return []
    
    result = []  # Store the reverse level order traversal
    
    # Perform BFS using a queue
    queue = [root]
    
    while queue:
        level_size = len(queue)
        level_values = []
        
        # Traverse all nodes in the current level
        for _ in range(level_size):
            node = queue.pop(0)
            level_values.append(node.data)
            
            # Enqueue children (if any)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Insert the level values at the beginning of the result list
        result.insert(0, level_values)
    
    # Flatten the result list and return
    return [val for level in result for val in level]
