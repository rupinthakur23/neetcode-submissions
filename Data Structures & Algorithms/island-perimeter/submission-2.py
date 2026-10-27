class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            if min(r,c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 1
            
            if ((r,c)) in visited:
                return 0
            
            visited.add((r,c))

            return (dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c -1))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return dfs(i,j)
