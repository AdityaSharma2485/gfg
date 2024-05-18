class Solution:
    def getMinDiff(self, arr, n, k):
        # Sort the array
        arr.sort()

        # Initialize the difference between the maximum and minimum heights
        ans = arr[-1] - arr[0]

        # Loop through the array and calculate the potential new heights
        for i in range(1, n):
            if arr[i] >= k:
                max_elem = max(arr[i - 1] + k, arr[-1] - k)
                min_elem = min(arr[0] + k, arr[i] - k)
                ans = min(ans, max_elem - min_elem)

        return ans
