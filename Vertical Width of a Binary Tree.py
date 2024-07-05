class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

from collections import deque

def verticalWidth(root):
    if not root:
        return 0
    
    # Use a deque to perform BFS
    queue = deque([(root, 0)])  # (node, horizontal_distance)
    
    # Use a set to store unique horizontal distances
    horizontal_distances = set()
    
    while queue:
        node, hd = queue.popleft()
        horizontal_distances.add(hd)
        
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    
    # The vertical width is the number of unique horizontal distances
    return len(horizontal_distances)
