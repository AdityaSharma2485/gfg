from typing import List

class Solution:
    def longestSubseq(self, n: int, a: List[int]) -> int:
        if n == 0:
            return 0

        # Initialize the dp array
        dp = [1] * n
        
        # Fill dp array using the given logic
        for i in range(1, n):
            for j in range(i):
                if abs(a[i] - a[j]) == 1:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # The result is the maximum value in the dp array
        return max(dp)
