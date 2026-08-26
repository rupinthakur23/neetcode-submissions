class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        queue = deque()

        def add(row, col):
            if board[row][col] == 'O':
                queue.append((row, col))
                board[row][col] = 'T'

        for row in range(ROWS):
            add(row,0)
            add(row,COLS - 1)

        for col in range(COLS):
            add(0, col)
            add(ROWS -1,col)

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()

                for dr, ds in directions:
                    newRow, newCol = row + dr, col + ds

                    if min(newRow, newCol) < 0 or newRow >= ROWS or newCol >= COLS or board[newRow][newCol] != 'O':
                        continue
                    
                    queue.append((newRow, newCol))
                    board[newRow][newCol] = 'T'
                
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == 'T':
                    board[row][col] = 'O'


        



