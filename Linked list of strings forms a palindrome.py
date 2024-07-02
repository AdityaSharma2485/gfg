class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def compute(head): 
    # Initialize an empty string to collect the concatenated result
    combined_string = ""
    
    # Traverse the linked list and concatenate the string data
    current = head
    while current is not None:
        combined_string += current.data
        current = current.next
    
    # Check if the concatenated string is a palindrome
    return combined_string == combined_string[::-1]

