class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        fresh = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col))
                    visited.add((row, col))
                if grid[row][col] == 1:
                    fresh +=1
        time = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc

                    if min(newRow, newCol) < 0 or newRow >= ROWS or newCol >= COLS or (newRow, newCol) in visited or grid[newRow][newCol] != 1:
                        continue
                    
                    grid[newRow][newCol] = 2
                    fresh -=1

                    q.append((newRow, newCol))
                    visited.add((newRow, newCol))
            
            time +=1
        
        return time if fresh == 0 else -1


