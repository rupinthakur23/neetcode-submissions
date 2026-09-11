# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def sameTree(p, q):

            if not q and not p:
                return True
            
            if p and q and p.val == q. val:
                return (sameTree(p.left, q.left) and sameTree(p.right, q.right))
            else:
                return False
        return sameTree(p, q)

        