# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def balanced(root):
            if not root:
                return [0, True]
            
            leftTree = balanced(root.left)
            rightTree = balanced(root.right)

            newHeight = 1 + max(leftTree[0], rightTree[0])

            if not leftTree[1] or not rightTree[1] or abs(leftTree[0] - rightTree[0]) > 1:
                return [newHeight, False]
            
            return [newHeight, True]
        

        return balanced(root)[1]
        