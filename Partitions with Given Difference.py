from typing import List

class Solution:
    def countPartitions(self, n: int, d: int, arr: List[int]) -> int:
        MOD = 10**9 + 7
        sum_arr = sum(arr)
        
        # If (sum_arr + d) is odd, it is impossible to split the array into two subsets
        if (sum_arr + d) % 2 != 0:
            return 0
        
        target = (sum_arr + d) // 2
        
        # Initialize the dp array
        dp = [0] * (target + 1)
        dp[0] = 1
        
        # Dynamic Programming to count the subsets with the target sum
        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] = (dp[j] + dp[j - num]) % MOD
        
        return dp[target]
