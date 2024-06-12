class Solution:
    def countNumberswith4(self, n : int) -> int:
        total = 0
        for i in range(1, n + 1):  # Include n in the range
            if '4' in str(i):  # Check if the digit '4' is in the number
                total += 1
                
        return total
