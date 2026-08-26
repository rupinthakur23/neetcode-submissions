class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols, count  = len(grid), len(grid[0]), 0

        def dfs(row, col):
            if min(row, col) < 0 or row >= rows or col >=cols or grid[row][col] == '0':
                return
            
            grid[row][col] = '0'

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count +=1
                    dfs(r,c)
        
        return count