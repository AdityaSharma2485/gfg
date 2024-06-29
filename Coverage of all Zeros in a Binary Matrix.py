class Solution:
    def findCoverage(self, matrix):
        # Get dimensions of the matrix
        n = len(matrix)
        m = len(matrix[0])
        
        # Initialize coverage counter
        coverage = 0
        
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Iterate through each cell in the matrix
        for i in range(n):
            for j in range(m):
                # If the cell contains 0
                if matrix[i][j] == 0:
                    # Check all four directions
                    for direction in directions:
                        ni, nj = i + direction[0], j + direction[1]
                        # Check if the neighboring cell is within bounds and is 1
                        if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == 1:
                            coverage += 1
        return coverage
