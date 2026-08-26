class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        length = 1

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i,j))

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()

                for dr, ds in directions:
                    newRow, newCol = row + dr, col + ds
                    if min(newRow, newCol) <0 or newRow >= ROWS or newCol >= COLS or (newRow, newCol) in visited or grid[newRow][newCol] == -1:
                        continue
                    
                    grid[newRow][newCol] = length
                    queue.append((newRow, newCol))
                    visited.add((newRow,newCol))
            length +=1

