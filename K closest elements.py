class Solution:
    def printKClosest(self, arr, n, k, x):
        id1 = self.findCrossOver(arr, 0, n - 1, x)
        id2 = id1 + 1
        if id1 >= 0 and arr[id1] == x:
            id1 -= 1
        ans = []
        for i in range(k):
            if id1 >= 0 and id2 < n:
                val1 = x - arr[id1]
                val2 = arr[id2] - x
                if val1 < val2:
                    ans.append(arr[id1])
                    id1 -= 1
                else:
                    ans.append(arr[id2])
                    id2 += 1
            elif id1 >= 0:
                ans.append(arr[id1])
                id1 -= 1
            else:
                ans.append(arr[id2])
                id2 += 1
        return ans

    def findCrossOver(self, arr, low, high, x):
        if arr[high] <= x:
            return high
        if arr[low] > x:
            return low
        mid = (low + high) // 2
        if arr[mid] <= x and (mid + 1 <= high and arr[mid + 1] > x):
            return mid
        elif arr[mid] < x:
            return self.findCrossOver(arr, mid + 1, high, x)
        else:
            return self.findCrossOver(arr, low, mid - 1, x)
