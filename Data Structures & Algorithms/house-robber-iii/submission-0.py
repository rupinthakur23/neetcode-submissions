# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return [0, 0]
            
            leftTree = dfs(node.left)
            rightTree = dfs(node.right)

            withRoot = node.val + leftTree[1] + rightTree[1]
            withoutTree = max(leftTree) + max(rightTree)

            return [withRoot, withoutTree]
        
        return max(dfs(root))