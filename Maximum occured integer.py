class Solution:
    def maxOccured(self, n, l, r, maxx):
        # Create a frequency array initialized to 0 of size maxx + 2
        freq = [0] * (maxx + 2)
        
        # Apply the difference array approach
        for i in range(n):
            freq[l[i]] += 1
            if r[i] + 1 <= maxx:
                freq[r[i] + 1] -= 1
        
        # Calculate the prefix sum and find the maximum occurred integer
        max_occurrence = freq[0]
        max_occurred_number = 0
        current_occurrence = freq[0]
        
        for i in range(1, maxx + 1):
            current_occurrence += freq[i]
            if current_occurrence > max_occurrence:
                max_occurrence = current_occurrence
                max_occurred_number = i
        
        return max_occurred_number
