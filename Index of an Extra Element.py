class Solution:
    def findExtra(self,n,a,b):
        # Calculate the sum of the arrays
        sum_a = sum(a)
        sum_b = sum(b)
        
        # Determine the difference in sums to find the extra element
        if sum_a > sum_b:
            ele = sum_a - sum_b
            for x in range(len(a)):
                if a[x] == ele:
                    return x
        else:
            ele = sum_b - sum_a
            for x in range(len(b)):
                if b[x] == ele:
                    return x
