class Solution:
    def getCount(self, n: int) -> int:
        if n == 1:
            return 10
        
        # Adjacency list representing the valid moves
        moves = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [2, 1, 3, 5],
            3: [3, 2, 6],
            4: [4, 1, 5, 7],
            5: [5, 2, 4, 6, 8],
            6: [6, 3, 5, 9],
            7: [7, 4, 8],
            8: [8, 5, 7, 9, 0],
            9: [9, 6, 8]
        }
        
        # Initialize dp array
        dp = [[0] * 10 for _ in range(n + 1)]
        
        # Base case: sequences of length 1
        for j in range(10):
            dp[1][j] = 1
        
        # Fill dp table
        for i in range(2, n + 1):
            for j in range(10):
                dp[i][j] = sum(dp[i-1][k] for k in moves[j])
        
        # Sum up the results for sequences of length n
        return sum(dp[n][j] for j in range(10))
