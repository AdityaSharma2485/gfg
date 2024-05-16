class Solution:
    def __init__(self):
        self.ans = 0

    def dfs(self, adj, vis, start):
        vis[start] = 1
        cnt = 0
        
        for it in adj[start]:
            if not vis[it]:
                res = self.dfs(adj, vis, it)
                if res % 2 == 0:
                    self.ans += 1
                else:
                    cnt += res
        
        return cnt + 1

    def minimumEdgeRemove(self, n, edges):
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0] - 1].append(edge[1] - 1)
            adj[edge[1] - 1].append(edge[0] - 1)
        
        vis = [0] * n
        self.dfs(adj, vis, 0)
        
        return self.ans
