from typing import List
import heapq

class Solution:
    def MinimumEffort(self, rows: int, columns: int, heights: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_effort = float('inf')
        
        # Define a priority queue for Dijkstra's algorithm
        pq = [(0, 0, 0)]  # (effort, row, column)
        min_effort = [[max_effort] * columns for _ in range(rows)]
        min_effort[0][0] = 0
        
        while pq:
            effort, row, col = heapq.heappop(pq)
            if row == rows - 1 and col == columns - 1:
                return effort
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < columns:
                    new_effort = max(effort, abs(heights[new_row][new_col] - heights[row][col]))
                    if new_effort < min_effort[new_row][new_col]:
                        min_effort[new_row][new_col] = new_effort
                        heapq.heappush(pq, (new_effort, new_row, new_col))
