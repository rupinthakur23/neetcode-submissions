class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    queue.append((r,c))
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        minutes = 0
        while queue and fresh >0:
            print(queue)
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                
                    if min(nr, nc) <0 or nr >=ROWS or nc >= COLS or grid[nr][nc] !=1:
                        continue
                    
                    grid[nr][nc] = 2
                    queue.append((nr,nc))
                    fresh -=1
            minutes+=1
        
        return minutes if fresh == 0 else -1




