# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')

        def dfs(root):
            nonlocal result
            if not root:
                return 0
            
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            result = max(root.val + left + right, result)

            return max(root.val + left, root.val + right)
        

        dfs(root)
        return result