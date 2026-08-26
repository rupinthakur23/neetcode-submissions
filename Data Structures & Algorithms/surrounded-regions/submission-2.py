class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        queue = deque()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for col in range(COLS):
                if board[0][col] == "O":
                    queue.append((0, col))
                    board[0][col] = 'T'

                if board[ROWS - 1][col] == "O":
                    queue.append((ROWS - 1, col))
                    board[ROWS - 1][col] = 'T'

        for row in range(ROWS):
                if board[row][0] == "O":
                    queue.append((row, 0))
                    board[row][0] = 'T'

                if board[row][COLS - 1] == "O":
                    queue.append((row, COLS - 1))
                    board[row][COLS - 1] = 'T'


        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()

                for dr, ds in directions:
                    newRow, newCol = row + dr, col + ds

                    if min(newRow, newCol) <0 or newRow >= ROWS or newCol >= COLS or board[newRow][newCol] in ["X", "T"]:
                        continue
                    board[newRow][newCol] = 'T'
                    queue.append((newRow, newCol))
        

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == 'T':
                    board[row][col] = 'O'

