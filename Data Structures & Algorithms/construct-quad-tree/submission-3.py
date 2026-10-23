"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def quadTree(n, row, col):
            isAllSame = True

            for i in range(n):
                for j in range(n):
                    if grid[row + i][col + j] !=  grid[row][col]:
                        isAllSame = False
                        break
            
            if isAllSame:
                return Node(grid[row][col], True)
            
            n = n//2

            topLeft = quadTree(n, row, col)
            topRight = quadTree(n, row, col + n)
            bottomright = quadTree(n, row + n, col + n)
            bottomLeft = quadTree(n, row + n, col)

            return Node(1, False, topLeft, topRight, bottomLeft, bottomright )
                
        return quadTree(len(grid), 0, 0)
        
