# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, lowest, highest):
            if not node:
                return True
            
            if node.val > lowest and node.val < highest:
                return (dfs(node.left, lowest,node.val)
                and dfs(node.right, node.val, highest) )
            else:
                return False
        
        return dfs(root, float("-inf"), float("inf"))
