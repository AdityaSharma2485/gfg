class ListNode:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None

class TreeNode:
    # Constructor to create a new tree node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

from collections import deque

def convert(head):
    if not head:
        return None
    
    # Create the root of the tree
    root = TreeNode(head.data)
    head = head.next
    
    # Use a queue to do level order traversal
    queue = deque([root])
    
    while head:
        # Get the current node from the queue
        current = queue.popleft()
        
        # Create the left child from the next node in the linked list
        if head:
            left_child = TreeNode(head.data)
            current.left = left_child
            queue.append(left_child)
            head = head.next
        
        # Create the right child from the next node in the linked list
        if head:
            right_child = TreeNode(head.data)
            current.right = right_child
            queue.append(right_child)
            head = head.next
    
    return root
