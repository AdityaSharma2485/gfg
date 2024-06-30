class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def delete_node(self, head, x):
        # If the list is empty
        if not head:
            return None
        
        # If the node to be deleted is the head node
        if x == 1:
            new_head = head.next
            if new_head:
                new_head.prev = None
            return new_head
        
        # Traverse the list to find the node at position x
        current = head
        count = 1
        while current and count < x:
            current = current.next
            count += 1
        
        # If the position is greater than the number of nodes
        if not current:
            return head
        
        # Delete the node
        if current.next:
            current.next.prev = current.prev
        
        if current.prev:
            current.prev.next = current.next
        
        return head
