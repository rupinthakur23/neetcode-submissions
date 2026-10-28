class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        ROWS, COLS = len(heights), len(heights[0])
        pacificQueue, atlanticQueue = deque(), deque()
        pacificVisited, atlanticVisited = set(), set()
        directions = [[0,1],[0,-1],[-1,0], [1,0]]

        def dfs(queue, visited):
            while queue:
                for _ in range(len(queue)):
                    r,c = queue.popleft()

                    for dr, dc in directions:
                        newRow, newCol = r + dr, c + dc

                        if min(newRow, newCol) < 0 or newRow >= ROWS or newCol >= COLS or (newRow, newCol) in visited or heights[newRow][newCol] < heights[r][c]:
                            continue
                        queue.append((newRow,newCol))
                        visited.add((newRow, newCol))

 
        for r in [0]:
            for c in range(COLS):
                pacificQueue.append((r,c))
                pacificVisited.add((r,c))
        
        for r in range(ROWS):
            for c in [0]:
                pacificQueue.append((r,c))
                pacificVisited.add((r,c))
        
        dfs(pacificQueue, pacificVisited)

        for r in [ROWS - 1]:
            for c in range(COLS):
                atlanticQueue.append((r,c))
                atlanticVisited.add((r,c))

        for r in range(ROWS):
            for c in [COLS - 1]:
                atlanticQueue.append((r,c))
                atlanticVisited.add((r,c))
        
        dfs(atlanticQueue, atlanticVisited)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atlanticVisited and (r,c) in pacificVisited:
                    result.append([r,c])
        
        return result

