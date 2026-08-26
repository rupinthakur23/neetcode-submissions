class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        result = []

        atlanticVisited = set()
        pacificVisited = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(queue, visited):
            while queue:
                for i in range(len(queue)):
                    row, col = queue.popleft()

                    for dr, ds in directions:
                        newRow, newCol = dr + row, ds + col

                        if min(newRow, newCol) < 0 or newRow >= ROWS or newCol >= COLS or heights[newRow][newCol] < heights[row][col] or (newRow, newCol) in visited:
                            continue
                        
                        queue.append((newRow, newCol))
                        visited.add((newRow, newCol))

        queue = deque()


        for r in range(ROWS):
            pacificVisited.add((r,0))
            queue.append((r, 0))

        for c in range(COLS):
            pacificVisited.add((0,c))
            queue.append((0, c))
        
        bfs(queue, pacificVisited)

        queue = deque()

        for r in range(ROWS):
            atlanticVisited.add((r,COLS - 1))
            queue.append((r,COLS - 1))

        for c in range(COLS):
            atlanticVisited.add((ROWS - 1,c))
            queue.append((ROWS - 1,c))

        bfs(queue, atlanticVisited)

        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in atlanticVisited and  (i,j) in pacificVisited:
                    result.append([i,j])
        
        return result
