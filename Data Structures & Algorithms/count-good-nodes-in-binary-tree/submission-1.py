# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = []

        def dfs(node, highest):
            if not node:
                return 
            if node.val >= highest:
                result.append(node.val)
            
            dfs(node.left, max(node.val, highest))
            dfs(node.right, max(node.val, highest))   

        dfs(root, float('-inf'))
        return len(result)





        