class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def arrangeCV(self, head):
        if not head or not head.next:
            return head
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        temp = head
        tail = None
        cons = 0
        length = 0
        
        # Count consonants and find the last node
        while temp:
            if temp.data not in vowels:
                cons += 1
            length += 1
            if not temp.next:
                tail = temp
            temp = temp.next
        
        # If no consonants or all consonants, return head as it is
        if cons == 0 or length == cons:
            return head
        
        # Move nodes before the first vowel to the end
        while head and head.data not in vowels:
            x = head
            head = head.next
            tail.next = x
            tail = x
            x.next = None
            cons -= 1
        
        temp = head
        prev = None
        
        # Rearrange nodes
        while cons > 0:
            if tail == temp:
                break
            if temp.data not in vowels:
                prev.next = temp.next
                tail.next = temp
                temp.next = None
                tail = temp
                cons -= 1
                temp = prev.next
            else:
                prev = temp
                temp = temp.next
        
        return head
