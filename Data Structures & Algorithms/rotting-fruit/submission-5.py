class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        freshFruit = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visited.add((i,j))
                if grid[i][j] == 1:
                    freshFruit += 1
        time = 0
        directions = [[0,1],[0,-1],[-1,0], [1,0]]

        while queue and freshFruit > 0:
            for _ in range(len(queue)):
                r,c = queue.popleft()

                for dr, dc in directions:
                    newRow, newCol = r + dr, c + dc

                    if min(newRow, newCol) < 0 or newRow >= ROWS or newCol >= COLS or (newRow, newCol) in visited or grid[newRow][newCol] != 1:
                        continue
                    queue.append((newRow,newCol))
                    visited.add((newRow, newCol))
                    grid[newRow][newCol] = 2
                    freshFruit -= 1
            time +=1
        
        return time if freshFruit == 0  else -1


