class Solution:
    def countWays(self, s1: str, s2: str) -> int:
        MOD = 10**9 + 7
        n = len(s1)
        m = len(s2)
        
        # Create a 2D dp array with (n+1) x (m+1) dimensions
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Initialize dp[i][0] = 1 for all i
        for i in range(n + 1):
            dp[i][0] = 1
        
        # Fill the dp table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD
                else:
                    dp[i][j] = dp[i - 1][j] % MOD
        
        return dp[n][m]
