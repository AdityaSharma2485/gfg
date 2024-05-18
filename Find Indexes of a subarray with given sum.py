from typing import List

class Solution:
    def subArraySum(self, arr: List[int], n: int, S: int) -> List[int]:
        curr_sum = arr[0]
        start = 0

        for i in range(1, n + 1):
            # While current sum exceeds the target sum, move the start pointer to the right
            while curr_sum > S and start < i - 1:
                curr_sum -= arr[start]
                start += 1

            # If current sum equals the target sum, return the 1-based index
            if curr_sum == S:
                return [start + 1, i]

            # Add this element to curr_sum if we haven't reached the end
            if i < n:
                curr_sum += arr[i]

        # If we reach here, then there is no subarray with the given sum
        return [-1]
