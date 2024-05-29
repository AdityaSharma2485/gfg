class Solution:
    def findWinner(self, n: int, x: int, y: int) -> int:
        # Create a boolean array dp where dp[i] will be True if Geek can win with i coins
        dp = [False] * (n + 1)
        
        # Base case: If there are 0 coins, Geek loses
        dp[0] = False
        
        # Fill dp array for all values from 1 to n
        for i in range(1, n + 1):
            # Check if there is a move that makes the opponent lose
            if i >= 1 and not dp[i - 1]:
                dp[i] = True
            elif i >= x and not dp[i - x]:
                dp[i] = True
            elif i >= y and not dp[i - y]:
                dp[i] = True
        
        # The result for n coins
        return 1 if dp[n] else 0
