## https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if not rows:
            return -1
        
        cols = len(grid[0])
        
        fresh = 0
    
        rotten = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        mins = 0

        while rotten and fresh>0:
            mins += 1
            # print("per min iteration", rotten, fresh, mins)

            for _ in range(len(rotten)):
                x,y = rotten.popleft()
                for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                    xx, yy = x+dx, y+dy
                    if xx<0 or xx==rows or yy<0 or yy==cols:
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy]==2:
                        continue
                    fresh -= 1
                    grid[xx][yy]=2
                    rotten.append((xx,yy))
            
                
        return mins if fresh==0 else -1
