## https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if (r*c) != (m*n):
            return mat
        else:
            ans = [[0] * c for _ in range(r)]
            for i in range(m * n):
                ans[i // c][i % c] = mat[i // n][i % n]
            return ans

## Fast solution
# class Solution:
#     def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
#         if (r*c) != (len(mat)*len(mat[0])):
#             return mat
#         else:
#             # zip(*([iter(flat)] * c))
#             flat = sum(mat, [])
#             return [[flat.pop(0) for j in range(c)] for i in range(r)]
            
        
## code writing optimized
# class Solution:
#     def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
#         if (r*c) != (len(mat)*len(mat[0])):
#             return mat
#         else:
#             flatList = [y for x in mat for y in x]
#             # print(flatList)
        
        
## Basic Solution
# class Solution:
#     def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
#         if (r*c) != (len(mat)*len(mat[0])):
#             return mat
#         else:
#             flatList = []
#             for subList in mat:
#                 for item in subList:
#                     flatList.append(item)
#             newMat = []
#             for i in range(0,len(flatList),c):
#                 newMat.append(flatList[i:i+c])
#             return newMat