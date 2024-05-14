
from typing import List
from collections import deque


class Solution:
    def bfs(self, adj: List[List[int]], start: int, vis: List[int]) -> bool:
        num, edges = 0, 0
        q = deque()
        q.append(start)
        vis[start] = 1
        
        while q:
            node = q.popleft()
            num += 1
            edges += len(adj[node])
            
            for neighbor in adj[node]:
                if not vis[neighbor]:
                    q.append(neighbor)
                    vis[neighbor] = 1
        
        return num * (num - 1) == edges
    
    def findNumberOfGoodComponent(self, e: int, v: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(v + 1)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        vis = [0] * (v + 1)
        ans = 0
        for i in range(1, v + 1):
            if self.bfs(adj, i, vis):
                ans += 1
        
        return ans
