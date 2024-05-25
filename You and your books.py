class Solution:
    def max_Books(self, n, k, arr):
        max_books = 0
        current_sum = 0
        start = 0
        
        for end in range(n):
            if arr[end] > k:
                # If the current stack height exceeds k, reset the window
                start = end + 1
                current_sum = 0
            else:
                # Add the current stack height to the current sum
                current_sum += arr[end]
                # Update the maximum number of books collected
                max_books = max(max_books, current_sum)
        
        return max_books
