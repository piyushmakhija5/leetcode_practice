## https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m , n = len(matrix), len(matrix[0])
        
        i = m-1
        j = 0
        while i>=0 and (j<n):
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False
            
