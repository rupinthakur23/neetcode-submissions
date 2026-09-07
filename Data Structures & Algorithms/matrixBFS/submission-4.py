class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:

        if grid[0][0] != 0:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()


        visited.add((0, 0))
        q.append((0,0))
        result = 0

        directions = [[1,0], [-1, 0], [0,1], [0,-1]]

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()

                if row == ROWS - 1 and col == COLS - 1:
                    return result 
                
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc

                    if min(newRow, newCol) < 0 or newRow >= ROWS or newCol>= COLS or (newRow, newCol) in visited or grid[newRow][newCol] != 0:
                        continue
                    q.append((newRow,newCol))
                    visited.add((newRow,newCol))
            
            result +=1
        
        return -1




