## https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            print(i, len(matrix), ((matrix[i][0] <= target) and (i<(len(matrix)-1)) and (matrix[i+1][0]>target)))
            if (i==len(matrix)-1) or ((matrix[i][0] <= target) and (matrix[i+1][0]>target)):
                ## traverse deeper
                for j in range(len(matrix[0])):
                    if matrix[i][j]==target:
                        return True
        return False
                    
