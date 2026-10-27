class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
        depth = 1
        directions = [[0,1],[0,-1],[-1,0], [1,0]]

        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()

                for dr, dc in directions:
                    newRow, newCol = r + dr, c + dc

                    if min(newRow, newCol) < 0 or newRow >= ROWS or newCol >= COLS or (newRow, newCol) in visited or grid[newRow][newCol] == -1:
                        continue
                    queue.append((newRow,newCol))
                    visited.add((newRow, newCol))
                    grid[newRow][newCol] = depth
            depth +=1


