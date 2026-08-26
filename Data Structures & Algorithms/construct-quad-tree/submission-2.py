"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def quadTree(n, r , c):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[i + r][j + c] != grid[r][c]:
                        allSame = False
            
            if allSame:
                return Node(grid[r][c],True)
            
            n = n//2
            
            topLeft = quadTree(n,r, c)
            topRight = quadTree(n,r, c + n)
            bottomLeft = quadTree(n,r + n, c)
            bottomRight = quadTree(n,r + n, c + n)

            return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)
        
    
        return quadTree(len(grid), 0, 0)