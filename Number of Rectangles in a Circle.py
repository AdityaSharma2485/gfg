class Solution:
    def rectanglesInCircle(self,r):
        count = 0
        max_side = 2 * r  # The maximum possible side length of the rectangle
        
        for w in range(1, max_side + 1):
            for h in range(1, max_side + 1):
                if w * w + h * h <= 4 * r * r:
                    count += 1
        
        return count
