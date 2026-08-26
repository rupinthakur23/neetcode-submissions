# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float("-inf")

        def maxPath(node):
            nonlocal result
            if not node:
                return 0
            left = max(maxPath(node.left), 0)
            right = max(maxPath(node.right), 0)  
            value = node.val + left + right
            result = max(result, value)
            return node.val + max(left, right)
        

        maxPath(root)
        return result
        