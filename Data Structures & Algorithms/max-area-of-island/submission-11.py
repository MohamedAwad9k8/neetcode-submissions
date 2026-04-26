class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, columns = len(grid), len(grid[0])
        max_size = 0
        visit = set()

        def bfs (r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            size = 1
            while q:
                r, c = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if (new_r in range(rows) and new_c in range(columns)
                        and grid[new_r][new_c] == 1 
                        and (new_r, new_c) not in visit):
                        q.append((new_r,new_c))
                        visit.add((new_r,new_c))
                        size += 1
            print ("New Island Found, Island Size: ", size)
            return size

        for row in range(rows):
            for column in range(columns):
                print (row, column)
                if grid[row][column] == 1 and ((row, column) not in visit):
                    print("BFS for ", row, column)
                    max_size = max (max_size, bfs(row, column))
                    
        return max_size