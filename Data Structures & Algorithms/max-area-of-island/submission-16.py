class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, columns = len(grid), len(grid[0])
        
        visit = set()
        def dfs(r,c):
            #base case
            if((r not in range(rows)) or (c not in range(columns))
                or grid[r][c] == 0 or (r,c) in visit):
                return 0
            visit.add((r,c))
            return (1 + dfs(r+1, c) + dfs(r-1, c) +
                dfs(r, c+1) + dfs(r, c-1))
        
        area = 0
        for row in range(rows):
            for column in range(columns):
                area = max (area, dfs(row,column))
        return area