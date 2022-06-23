class Solution:
    
    def searchInRow(self, row: List[int], target: int) -> bool:
        l, r = 0, len(row) - 1
        while l <= r:
            i = (l + r) // 2
            if row[i] == target:
                return True
            if row[i] > target:
                r = i - 1
            elif row[i] < target:
                l = i + 1
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row, r_row = 0, len(matrix) - 1
        l_col, r_col = 0, len(matrix[0]) - 1
        while l_row <= r_row:
            row_i = (l_row + r_row) // 2
            if matrix[row_i][l_col] <= target and matrix[row_i][r_col] >= target:
                return self.searchInRow(matrix[row_i], target)
            elif matrix[row_i][l_col] > target:
                r_row = row_i - 1
            elif matrix[row_i][r_col] < target:
                l_row = row_i + 1
        return False
      
