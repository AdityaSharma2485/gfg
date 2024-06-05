class Solution:
    def findSwapValues(self, a, n, b, m):
        sumA = sum(a)
        sumB = sum(b)
        
        # If the difference is not even, there's no way to balance the arrays
        if (sumA - sumB) % 2 != 0:
            return -1
        
        target = (sumA - sumB) // 2
        
        # Convert list b to set for O(1) look-up times
        setB = set(b)
        
        # Check for each element in a if there exists an element in b
        for x in a:
            if x - target in setB:
                return 1
        
        return -1
