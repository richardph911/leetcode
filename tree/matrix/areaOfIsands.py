class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r,c):
            if (r<0 or c <0 or r >= rows or c >= cols or (r,c) in visit or grid[r][c]==0):
                return 0
            visit.add((r,c))
            #cal area
            return (1 + dfs(r+1,c)+dfs(r-1,c)+dfs(r, c+1)+dfs(r,c-1))
        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                maxArea = max(maxArea, dfs(i, j))
        return maxArea       