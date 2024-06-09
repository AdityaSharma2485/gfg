from typing import List

class Solution:
    def zigZag(self, n: int, arr: List[int]) -> None:
        # Iterate through the array
        for i in range(n - 1):
            if i % 2 == 0:
                # "Less than" condition for even index
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            else:
                # "Greater than" condition for odd index
                if arr[i] < arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
