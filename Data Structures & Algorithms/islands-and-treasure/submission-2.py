class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        distance = 1

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row,col))
                    visited.add((row,col))
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
    
        while q:
            for _ in range(len(q)):

                row, col = q.popleft()

                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    if min(newRow, newCol) <0 or newRow >= ROWS or newCol >= COLS or grid[newRow][newCol] in [0,-1] or (newRow, newCol) in visited:
                        continue
                    
                    grid[newRow][newCol] = distance
                    q.append((newRow, newCol))
                    visited.add((newRow, newCol))
            distance +=1
        




