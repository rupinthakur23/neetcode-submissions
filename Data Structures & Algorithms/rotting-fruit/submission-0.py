class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        minute, fresh = 0, 0
        startExists = False

        queue = deque()


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh +=1 



        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                        
                for dr, dc in directions:
                    newRow, newCol = dr + r, dc + c
                    if min(newRow, newCol) <0 or newRow>= ROWS or newCol >= COLS or grid[newRow][newCol] in [0,2]:
                        continue
                    grid[newRow][newCol] = 2
                    queue.append((newRow, newCol))
                    fresh -=1
            minute +=1
        return minute if fresh == 0 else -1

        
        