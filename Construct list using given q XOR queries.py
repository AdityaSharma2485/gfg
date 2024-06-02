from typing import List

class Solution:
    def constructList(self, q: int, queries: List[List[int]]) -> List[int]:
        # Initialize the list with a single element 0
        s = [0]
        # Initialize cumulative XOR value
        cumulative_xor = 0
        
        # Iterate over each query and perform the corresponding operation
        for query in queries:
            if query[0] == 0:
                # Insert x into the list
                x = query[1]
                # Insert x directly without applying XOR now
                s.append(x ^ cumulative_xor)
            elif query[0] == 1:
                # Update the cumulative XOR value
                cumulative_xor ^= query[1]
        
        # Apply the cumulative XOR to all elements in the list
        s = [a ^ cumulative_xor for a in s]
        
        # Sort the list before returning
        s.sort()
        return s
