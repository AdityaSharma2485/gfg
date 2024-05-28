from typing import List

class Solution:
    def minimumCost(self, n: int, w: int, cost: List[int]) -> int:
        # Initialize dp array with infinity. dp[j] will be the minimum cost to get exactly j kg of oranges.
        dp = [float('inf')] * (w + 1)
        
        # Base case: 0 kg of oranges costs 0.
        dp[0] = 0
        
        # Fill the dp array.
        for j in range(1, w + 1):
            for i in range(1, n + 1):
                if i <= j and cost[i - 1] != -1:
                    dp[j] = min(dp[j], dp[j - i] + cost[i - 1])
        
        # If dp[w] is still infinity, it means it's not possible to get exactly w kg of oranges.
        return dp[w] if dp[w] != float('inf') else -1
