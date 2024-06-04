class Solution:
    def numberOfConsecutiveOnes(self, n):
        MOD = int(1e9 + 7)
        
        if n == 1:
            return 0
        
        # Create dp array
        dp = [0] * (n + 1)
        
        # Base cases
        dp[1] = 2  # "0", "1"
        dp[2] = 3  # "00", "01", "10"
        
        # Fill the dp array using the recurrence relation
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
        
        # Total number of binary strings of length n
        total_strings = pow(2, n, MOD)
        
        # Number of strings without consecutive 1's
        valid_strings = dp[n]
        
        # Number of strings with consecutive 1's
        result = (total_strings - valid_strings + MOD) % MOD
        
        return result
