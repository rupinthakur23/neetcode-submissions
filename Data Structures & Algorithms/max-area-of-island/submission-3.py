class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        result = 0

        def dfs(row, col):

            if min(row, col) <0 or row >= ROWS or col >=COLS or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0

            count = 1

            count += (dfs(row + 1, col) + dfs(row - 1, col) + dfs(row , col + 1) + dfs(row , col - 1))

            return count

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    result = max(dfs(row, col), result)
            
        return result
        
        