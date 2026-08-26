class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row,col))
                    visited.add((row,col))

        length = 1
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()

                for dr, ds in directions:
                    newRow, newCol = row + dr, col + ds
 
                    if min(newRow, newCol) <0 or newRow >= ROWS or newCol >= COLS or grid[newRow][newCol] == -1 or (newRow,newCol) in visited:
                        continue
  
                    grid[newRow][newCol] = length

                    queue.append((newRow,newCol))
                    visited.add((newRow,newCol))
        
            length+=1

