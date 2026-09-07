class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col, visited):
            if min(row, col) <0 or row >= ROWS or col >= COLS or (row, col) in visited or grid[row][col] == 1:
                return 0

            if row == ROWS - 1 and col == COLS - 1:
                return 1
            
            visited.add((row, col))

            count = (dfs(row + 1, col, visited) + dfs(row - 1, col, visited) + dfs(row, col + 1, visited) + dfs(row, col - 1, visited))
            visited.remove((row, col))
            return count

        return dfs(0, 0, set())