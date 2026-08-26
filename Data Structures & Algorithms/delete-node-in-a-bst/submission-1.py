# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        curr = root

        if curr.val > key:
            curr.left = self.deleteNode(curr.left, key)
        elif curr.val < key:
            curr.right =  self.deleteNode(curr.right, key)
        else:
            if not curr.left:
                return curr.right
            if not curr.right:
                return curr.left
            
            node = self.minNode(curr.right)

            curr.val = node

            curr.right = self.deleteNode(curr.right, node)

        return curr


    def minNode(self, node):
        curr = node
        while(curr and curr.left):
            curr = curr.left
        
        return curr.val