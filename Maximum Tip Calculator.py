from typing import List

class Solution:
    def maxTip(self, n: int, x: int, y: int, arr: List[int], brr: List[int]) -> int:
        # Create a list of tuples with each tuple containing (tip by A, tip by B, difference)
        orders = [(arr[i], brr[i], abs(arr[i] - brr[i])) for i in range(n)]
        
        # Sort orders based on the absolute difference in descending order
        orders.sort(key=lambda x: x[2], reverse=True)
        
        total_tips = 0
        countA = 0
        countB = 0
        
        for a_tip, b_tip, _ in orders:
            if (a_tip >= b_tip and countA < x) or countB == y:
                # Assign to A if A's tip is higher or if B has reached their limit
                total_tips += a_tip
                countA += 1
            else:
                # Assign to B if B's tip is higher or if A has reached their limit
                total_tips += b_tip
                countB += 1
        
        return total_tips
