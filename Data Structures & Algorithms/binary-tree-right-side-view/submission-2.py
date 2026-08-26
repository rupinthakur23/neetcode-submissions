# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, depth):
            nonlocal result
            if not node:
                return 0
            
            if len(result) == depth:
                result.append(node.val)
            
            dfs(node.right, 1 + depth)
            dfs(node.left, 1 + depth)
        
        dfs(root, 0)
        return result