# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float("-inf")

        def dfs(node):
            nonlocal result
            if not node:
                return 0
            
            leftPath = max(dfs(node.left), 0)
            rightPath = max(dfs(node.right), 0)

            result = max(node.val + leftPath + rightPath, result)

            return node.val + max(leftPath, rightPath)
        dfs(root)
        return result