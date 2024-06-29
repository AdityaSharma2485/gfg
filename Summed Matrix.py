class Solution:
    def sumMatrix(self, n, q):
        # Calculate the range of i
        start = max(1, q - n)
        end = min(n, q - 1)
        
        # Calculate the count of valid (i, j) pairs
        count = max(0, end - start + 1)
        
        return count
