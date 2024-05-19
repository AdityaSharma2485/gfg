from typing import List


class Solution:
    def findClosest(self, n : int, target : int, arr : List[int]) -> int:
        # Corner cases
        if (target <= arr[0]):
            return arr[0]
        if (target >= arr[n - 1]):
            return arr[n - 1]
     
        # Doing binary search
        i = 0; j = n; mid = 0
        while (i < j): 
            mid = (i + j) // 2
     
            if (arr[mid] == target):
                return arr[mid]
     
            # If target is less than array 
            # element, then search in left
            if (target < arr[mid]) :
     
                # If target is greater than previous
                # to mid, return closest of two
                if (mid > 0 and target > arr[mid - 1]):
                    return getClosest(arr[mid - 1], arr[mid], target)
     
                # Repeat for left half 
                j = mid
             
            # If target is greater than mid
            else :
                if (mid < n - 1 and target < arr[mid + 1]):
                    return getClosest(arr[mid], arr[mid + 1], target)
                     
                # update i
                i = mid + 1
             
        # Only single element left after search
        return arr[mid]
        

def getClosest(val1, val2, target):
 
    if (target - val1 >= val2 - target):
        return val2
    else:
        return val1
