# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def backtracking(root, targetSum, total):
            if not root:
                return False
            
            total += root.val

            if not root.left and not root.right and total == targetSum:
                return True
            
            if backtracking(root.left, targetSum, total):
                return True

            if backtracking(root.right, targetSum, total):
                return True
            
            total -= root.val

            return False

        return backtracking(root, targetSum, 0)