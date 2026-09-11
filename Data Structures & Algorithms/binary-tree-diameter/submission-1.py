# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def calculateDiameter(root):
            nonlocal result
            if not root:
                return 0
            
            leftValue =  calculateDiameter(root.left)
            rightValue = calculateDiameter(root.right)
            result = max(result, leftValue + rightValue)
            return 1 + max(leftValue, rightValue)

        calculateDiameter(root)
        return result