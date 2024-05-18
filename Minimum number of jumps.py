class Solution:
	def minJumps(self, arr, n):
	    if n <= 1:
            return 0  # No jumps needed if array has one or no element
        
        if arr[0] == 0:
            return -1  # Cannot move anywhere if the first element is 0
        
        # Initialize maximum reachable index, steps we can still take, and the number of jumps
        maxReach = arr[0]
        step = arr[0]
        jump = 1

        for i in range(1, n):
            # If we have reached the last element, return the number of jumps
            if i == n - 1:
                return jump

            # Update the maximum reachable index
            maxReach = max(maxReach, i + arr[i])
            
            # Use a step to move to the current index
            step -= 1
            
            # If no more steps are remaining
            if step == 0:
                # We must have used a jump
                jump += 1

                # Check if the current index is reachable
                if i >= maxReach:
                    return -1  # If we cannot move further
                
                # Reinitialize steps to the amount of steps to reach maxReach from position i
                step = maxReach - i

        return -1
