class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def findAncestors(self, root, target, ancestors):
        if root is None:
            return False

        if root.data == target:
            return True

        if (self.findAncestors(root.left, target, ancestors) or
                self.findAncestors(root.right, target, ancestors)):
            ancestors.append(root.data)
            return True

        return False

    def Ancestors(self, root, target):
        ancestors = []
        self.findAncestors(root, target, ancestors)
        return ancestors
