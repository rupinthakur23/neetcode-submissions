# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs(root, rootVal):
            nonlocal result

            if not root:
                return
            
            if root.left:
                dfs(root.left, max(root.left.val, rootVal))

            if root.right:
                dfs(root.right, max(root.right.val, rootVal))

            if root.val >= rootVal:
                result +=1
        
        dfs(root, root.val)
        return result