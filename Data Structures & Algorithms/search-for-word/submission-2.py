class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, target):
            if min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in visited or word[target] != board[r][c]:
                return False
            
            visited.add((r,c))

            if len(word) -1 == target:
                return True
            
            result = (dfs(r + 1, c, target + 1) or  dfs(r - 1, c, target + 1) or dfs(r, c + 1, target + 1) or dfs(r, c - 1, target + 1))

            visited.remove((r,c))

            return result
            
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j, 0):
                    return True
        
        return False
        