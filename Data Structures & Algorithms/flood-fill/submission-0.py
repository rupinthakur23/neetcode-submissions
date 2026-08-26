class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def dfs(image, sr, sc, startingColor):
            row, col = len(image), len(image[0])

            if min(sr, sc) <0 or sr >= row or sc >=col or image[sr][sc] != startingColor or image[sr][sc] == color:
                return
            else:
                image[sr][sc] = color

            dfs(image, sr + 1, sc, startingColor)
            dfs(image, sr - 1, sc, startingColor)
            dfs(image, sr , sc + 1, startingColor)
            dfs(image, sr, sc - 1, startingColor)


        dfs(image, sr, sc, image[sr][sc])
        return image

        