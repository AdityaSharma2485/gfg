class Solution:
    def KDistance(self, root, k):
        def dfs(node, distance):
            if not node:
                return []
            if distance == k:
                return [node.data]
            return dfs(node.left, distance + 1) + dfs(node.right, distance + 1)

        return dfs(root, 0)
