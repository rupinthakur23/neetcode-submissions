class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        if grid[ROWS - 1][COLS - 1] == 1 or grid[0][0] == 1:
            return -1
        
        queue = deque()
        visit = set()

        queue.append((0, 0))
        visit.add((0, 0))

        length = 1

        directions = [[1,0], [-1,0], [0,1], [0, -1], [1, -1], [1, 1], [-1, -1], [-1, 1]]

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length

                for dr, dc in directions:
                    newRow, newCol = dr + r, dc + c

                    if min(newRow, newCol) <0 or newRow>= ROWS or newCol >= COLS or (newRow, newCol) in visit or grid[newRow][newCol] == 1:
                        continue
                    queue.append((newRow, newCol))
                    visit.add((newRow, newCol))
            length +=1
        
        return -1
                    
