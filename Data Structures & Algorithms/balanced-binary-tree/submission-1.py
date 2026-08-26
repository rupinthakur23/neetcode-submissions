# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, height):
            if not node:
                return [True,0]
            
            left = dfs(node.left, height)
            right = dfs(node.right,  height)

            if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
                return [True, 1 + max(left[1],right[1])]
            else:
                return [False, 1 + max(left[1],right[1])]
        
        result = dfs(root, 0)  
        return result[0]      
