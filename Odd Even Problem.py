class Solution:
    def oddEven(self, s : str) -> str:
        from collections import Counter
        
        # Step 1: Calculate frequency of each character
        freq = Counter(s)
        
        # Initialize counters for x and y
        x = 0
        y = 0
        
        # Step 2: Classify characters
        for char, count in freq.items():
            position = ord(char) - ord('a') + 1  # Position in alphabet (1-based index)
            
            if position % 2 == 0:  # Even position
                if count % 2 == 0:  # Even frequency
                    x += 1
            else:  # Odd position
                if count % 2 != 0:  # Odd frequency
                    y += 1
        
        # Step 3: Sum x and y and check parity
        if (x + y) % 2 == 0:
            return "EVEN"
        else:
            return "ODD"
