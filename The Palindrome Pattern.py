class Solution:
    def pattern(self, arr):
        n = len(arr)
        
        # Check each row
        for i in range(n):
            if arr[i] == arr[i][::-1]:  # Check if the row is a palindrome
                return "{} R".format(i)
        
        # Check each column
        for j in range(n):
            column = [arr[i][j] for i in range(n)]
            if column == column[::-1]:  # Check if the column is a palindrome
                return "{} C".format(j)
        
        return "-1"
