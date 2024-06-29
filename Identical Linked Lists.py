class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Function to check whether two linked lists are identical or not.
def areIdentical(head1, head2):
    # Traverse both lists simultaneously
    while head1 is not None and head2 is not None:
        # Compare data of both nodes
        if head1.data != head2.data:
            return False
        # Move to the next nodes
        head1 = head1.next
        head2 = head2.next
    
    # If one list is not null, it means lists are of different lengths
    return head1 is None and head2 is None
