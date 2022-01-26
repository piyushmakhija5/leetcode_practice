## https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalT = [[1]*(i+1) for i in range(numRows)]
        for i in range(2,numRows):
            for j in range(1,i):
                # print(i,j, pascalT)
                pascalT[i][j] = pascalT[i-1][j-1] + pascalT[i-1][j]
        return pascalT
    
## Basic code
# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         pascalT = []
#         for row in range(numRows):
#             # print("row #", row)
#             if row == 0:
#                 pascalT.append([1])
#             elif row == 1:
#                 pascalT.append([1,1])
#             else:
#                 val = []
#                 for item in range(row+1):
#                     if (item == 0) or (item == row):
#                         val.append(1)
#                     else:
#                         # print(item, pascalT[row-1])
#                         val.append(pascalT[row-1][item-1] + pascalT[row-1][item])
#                 # print("val:", val)
#                 pascalT.append(val)
#             # print(pascalT)
#         return pascalT
