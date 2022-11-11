## https://leetcode.com/problems/spiral-matrix-ii/

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ## Walk the spiral
        A = [[0]*n for _ in range(n)]
        i, j, di, dj = 0,0,0,1
        for k in range(n*n):
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A
        
        ## BUild matrix inside-out -> not working !!
        # A = [[n*n]]
        # while A[0][0] > 1:
        #     A = [range(A[0][0] - len(A), A[0][0])] + zip(*A[::-1])
        # return A * (n>0)
        
        ## Sprial order
        # i=0, j=0
        # i:0->n, j:1->n, i:n-1->0, j:n-1->1, i:1:
#         if n==1:
#             return [[1]]
#         else:
#             res = [[0 for i in range(n)] for j in range(n)]
#             r1 = 0
#             r2 = n -1 
#             c1 = 0
#             c2 = n -1
#             k = 1 
            
#             while (r1<=r2) and (c1<=c2):
#                 for i in range(r1,r2+1):
#                     res[c1][i] = k
#                     k += 1
#                 for i in range(c1+1,c2+1):
#                     res[i][r2] = k
#                     k+=1
#                 for i in range(r2-1, r1-1, -1):
#                     res[c2][i] = k
#                     k += 1
#                 for i in range(c2-1, c1, -1):
#                     res[i][r1] = k
#                     k += 1
                
#                 r1 += 1
#                 c1 += 1
#                 r2 -= 1
#                 c2 -= 1
#         return res
                    
                
