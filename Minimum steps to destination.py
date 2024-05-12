class Solution:
    def minSteps(self, d):
        d = abs(d)
        sum_val = 0
        steps = 0
        
        while sum_val < d or abs(sum_val - d) % 2 != 0:
            steps += 1
            sum_val += steps
        
        return steps
