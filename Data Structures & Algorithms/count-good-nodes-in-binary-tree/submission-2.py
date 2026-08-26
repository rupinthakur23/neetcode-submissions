# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs(node, highest):
            nonlocal result

            if not node:
                return
            
            if node.val >= highest:
                result +=1
            
            dfs(node.left, max(highest, node.val))
            dfs(node.right, max(highest, node.val))
        
        dfs(root, root.val)
        return result
