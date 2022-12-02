## https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        matrix = heights
        if not heights:
            return []
        pac, atl = set(), set()
        m,n = len(heights), len(heights[0])
        
        
        for i in range(n):
            self.dfs(0, i, heights, pac, -1)
            self.dfs(m-1, i, heights, atl, -1)
        for i in range(m):
            self.dfs(i, 0, heights, pac, -1)
            self.dfs(i, n-1, heights, atl, -1)
        return list(pac & atl)
        
    def dfs(self,i,j,heights,explored,prev):
        m,n = len(heights),len(heights[0])
        if i<0 or i==m or j<0 or j==n or (i,j) in explored:
            return
        if heights[i][j] < prev:
            return
        explored.add((i,j))
        self.dfs(i-1,j,heights,explored,heights[i][j]) #up
        self.dfs(i+1,j,heights,explored,heights[i][j]) #down
        self.dfs(i,j-1,heights,explored,heights[i][j]) #left
        self.dfs(i,j+1,heights,explored,heights[i][j]) #right
