# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        if not root:
            return result
        
        def dfs(node, highest):
            nonlocal result
            if not node:
                return 0
            
            if highest <= node.val:
                result +=1
                highest = node.val
            
            dfs(node.left, highest)
            dfs(node.right, highest)

        dfs(root, root.val)
        return result
            