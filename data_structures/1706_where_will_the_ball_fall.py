## https://leetcode.com/problems/where-will-the-ball-fall/

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:    
        # Recursive approach: O(MN) time complexity, O(M) space complexity
        m, n = len(grid), len(grid[0])
        
        def dfs(i,j):
            if i==m:
                return j
            elif 0 <= (j_new := j + grid[i][j]) < n and grid[i][j] == grid[i][j_new]:
                    return dfs(i+1, j_new)
            else:
                return -1
        return [dfs(0,j) for j in range(n)]
