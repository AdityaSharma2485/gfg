class Solution:
    def findPair(self, n, x, arr):
        arr.sort()
        i, j = 0, 1
        
        while j < n:
            diff = abs(arr[j] - arr[i])
            
            if diff == x:
                return 1
            elif diff < x:
                j += 1
            else:
                i += 1
                
            # Avoid i and j pointing to the same element
            if i == j:
                j += 1
        
        return -1

