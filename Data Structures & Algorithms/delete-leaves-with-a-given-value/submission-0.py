# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def deleteLeaf(node):
            if not node:
                return node
            
            node.left = deleteLeaf(node.left)
            node.right = deleteLeaf(node.right)

            if node.val == target and not node.left and not node.right:
                return node.left
            else:
                return node

        
        return deleteLeaf(root)
