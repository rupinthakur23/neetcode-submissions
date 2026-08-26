class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        def dfs(grid, row, col, visited):
            ROWS = len(grid)
            COLS = len(grid[0])

            if min(row, col) < 0 or row >= ROWS or col >= COLS or grid[row][col] == 1 or (row, col) in visited:
                return 0

            if row == ROWS -1 and col == COLS - 1:
                return 1
            
            visited.add((row, col))

            count = 0

            count += dfs(grid, row - 1, col, visited)
            count += dfs(grid, row + 1, col, visited)
            count += dfs(grid, row, col - 1, visited)
            count += dfs(grid, row, col + 1, visited)


            visited.remove((row, col))

            return count


        return dfs(grid, 0, 0, set())
        