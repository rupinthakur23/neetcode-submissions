# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = 0 
        def dfs(node):
            nonlocal result
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            result = 1 + max(left, right)
            return result
        
        dfs(root)
        return result