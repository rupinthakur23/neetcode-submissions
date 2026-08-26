class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS =len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1
        visit = set()
        queue = deque()
        queue.append((0,0))
        visit.add((0,0))

        length = 0

        directions = [[1,0], [-1,0], [0,1], [0, -1]]


        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                for dr, dc in directions:
                    newRow, newCol = r + dr, c + dc

                    if min(newRow, newCol) <0 or newRow >= ROWS or newCol>=COLS or (newRow, newCol) in visit or grid[newRow][newCol] == 1:
                        continue
                    
                    queue.append((newRow, newCol))
                    visit.add((newRow, newCol))
            length +=1
        
        return -1 



        









        return length