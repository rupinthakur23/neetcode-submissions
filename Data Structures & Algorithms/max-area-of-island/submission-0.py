class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols, result  = len(grid), len(grid[0]), 0

        def dfs(r, c):
            if min(r,c) < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0 
            grid[r][c] = 0
            count = 0

            count +=1


            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)

            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result = max(dfs(r,c), result)
        
        return result
