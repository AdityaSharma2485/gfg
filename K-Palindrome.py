class Solution:
    def kPalindrome(self, str: str, n: int, k: int) -> bool:
        # Initialize a 2D DP array
        dp = [[0] * n for _ in range(n)]
        
        # Fill the DP table
        for length in range(2, n+1):  # length of the substring
            for i in range(n - length + 1):
                j = i + length - 1  # Ending index of the substring
                if str[i] == str[j]:
                    dp[i][j] = dp[i+1][j-1] if j > i + 1 else 0
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
        
        # The minimum deletions to make the entire string a palindrome
        return 1 if dp[0][n-1] <= k else 0
