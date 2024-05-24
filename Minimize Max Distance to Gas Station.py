import math
from typing import List

class Solution:
    def numberOfGasStationsRequired(self, dist: float, arr: List[int]) -> int:
        cnt = 0
        for i in range(1, len(arr)):
            gap = arr[i] - arr[i - 1]
            cnt += math.ceil(gap / dist) - 1
        return cnt

    def findSmallestMaxDist(self, stations: List[int], K: int) -> float:
        low, high = 0, max(stations[i + 1] - stations[i] for i in range(len(stations) - 1))

        diff = 1e-6
        while high - low > diff:
            mid = (low + high) / 2.0
            cnt = self.numberOfGasStationsRequired(mid, stations)
            if cnt > K:
                low = mid
            else:
                high = mid

        return high
