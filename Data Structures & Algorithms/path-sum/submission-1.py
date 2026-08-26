# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        result = 0

        def dfs(node):
            nonlocal result

            if not node:
                return False
            
            result += node.val

            if not node.left and not node.right:
                if result == targetSum:
                    return True
                else:
                    result -= node.val
                    return False
            
            if dfs(node.left):
                return True

            if dfs(node.right):
                return True

            result -= node.val
            
            return False
        
        return dfs(root)