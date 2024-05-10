class Solution:
    
    def CombinationSum2(self, arr, n, k):
        def CombinationSum2Util(arr, k, index, current, result):
            if k == 0:
                result.append(current[:])
                return

            if k < 0 or index == len(arr):
                return

            # Include the current element
            current.append(arr[index])
            CombinationSum2Util(arr, k - arr[index], index + 1, current, result)
            current.pop()

            # Exclude the current element and move to the next
            while index < len(arr) - 1 and arr[index] == arr[index + 1]:
                index += 1
            CombinationSum2Util(arr, k, index + 1, current, result)

        arr.sort()
        result = []
        CombinationSum2Util(arr, k, 0, [], result)
        return result
