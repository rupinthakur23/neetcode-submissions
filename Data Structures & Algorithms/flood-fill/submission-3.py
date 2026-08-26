class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        originalColor = image[sr][sc]

        def dfs(row, col):
            ROWS, COLS = len(image), len(image[0])

            if min(row, col) <0 or row >= ROWS or col >=COLS or image[row][col] != originalColor:
                return
            
            image[row][col] = color

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row , col + 1)
            dfs(row , col - 1)

            return

        dfs(sr, sc)
        return image

        