# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinimumNode(self, node):
        while node and node.left:
            node = node.left
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        curr = root

        if curr.val > key:
            curr.left = self.deleteNode(curr.left, key)
        elif curr.val < key:
            curr.right = self.deleteNode(curr.right, key)
        else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            else:
                minNode = self.findMinimumNode(curr.right)
                curr.val = minNode.val
                curr.right = self.deleteNode(curr.right, minNode.val)

        return root