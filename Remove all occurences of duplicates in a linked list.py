class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def removeAllDuplicates(self, head: Node) -> Node:
        if not head:
            return None
        
        dummy = Node(0)
        dummy.next = head
        prev = dummy
        current = head
        
        while current:
            # If it's a start of duplicates sublist, move till the end of duplicates sublist
            if current.next and current.data == current.next.data:
                while current.next and current.data == current.next.data:
                    current = current.next
                # Skip all duplicates
                prev.next = current.next
            else:
                # Otherwise, move `prev` pointer
                prev = prev.next
            
            # Move `current` pointer
            current = current.next
        
        return dummy.next
