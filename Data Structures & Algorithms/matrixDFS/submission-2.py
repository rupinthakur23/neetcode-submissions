class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(row, col):
            ROWS, COLS = len(grid), len(grid[0])

            if min(row, col) < 0 or row >= ROWS or col >= COLS or grid[row][col] == 1 or (row, col) in visited:
                return 0
            
            if row == ROWS - 1 and col == COLS - 1:
                return 1
            count = 0
            visited.add((row, col))

            count += (dfs(row + 1, col) + dfs(row - 1, col) + dfs(row , col + 1) + dfs(row, col - 1))
            visited.remove((row, col))
            return count

        return dfs(0, 0)