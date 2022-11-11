## https://leetcode.com/problems/pascals-triangle-ii/


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascalT = [[1]*(i+1) for i in range(rowIndex+1)]
        for row in range(2, rowIndex+1):
            for col in (range(1,row)):
                pascalT[row][col] =  pascalT[row-1][col-1] + pascalT[row-1][col]
                # print(row, col, pascalT)
        return pascalT[rowIndex]
                
                
