from collections import defaultdict

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Solution:
    def printAllDups(self, root):
        def foo(root, ans, d):
            if root is None:
                return "N"
            s = str(root.data) + foo(root.left, ans, d) + foo(root.right, ans, d)
            d[s] += 1
            if d[s] == 2:
                ans.append(root)
            return s
            
        ans = []
        d = defaultdict(int)
        foo(root, ans, d)
        return ans
