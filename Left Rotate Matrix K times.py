class Solution:
    def rotateMatrix(self, k, mat):
        rows = len(mat)
        cols = len(mat[0])
        
        # Function to rotate a row left by k positions
        def rotate_row_left(row, k):
            k = k % cols  # To handle cases where k > number of columns
            return row[k:] + row[:k]
        
        # Rotate each row
        new_matrix = [rotate_row_left(mat[i], k) for i in range(rows)]
        
        return new_matrix
