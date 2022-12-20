## https://leetcode.com/problems/01-matrix/description/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ## Using DP: forward pass and back pass reuiqred in both top->down + left->right fashion
        INT_MAX = 2**31-1
        m = len(mat)
        n = len(mat[0])

        dist = [[INT_MAX for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if i>0:
                        dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
                    if j>0:
                        dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i < m-1:
                        dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
                if j < n-1:
                        dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
        return dist


        ## O((m*n)^2) --> Time limit exceeded --> Brute force solution
        # INT_MAX = 2**31-1
        # m = len(mat)
        # n = len(mat[0])

        # dist = [[INT_MAX for _ in range(n)] for _ in range(m)]

        # for i in range(m):
        #     for j in range(n):
        #         if mat[i][j] == 0:
        #             dist[i][j] = 0
        #         else:
        #             for k in range(m):
        #                 for l in range(n):
        #                     if mat[k][l]==0:
        #                         distance = abs(k-i) + abs(l-j)
        #                         dist[i][j] = min(dist[i][j], distance)
        # return dist
