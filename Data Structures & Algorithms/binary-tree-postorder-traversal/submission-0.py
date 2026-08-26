# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result, stack, v = [], [root], [False]

        while stack:
            curr, visited = stack.pop(), v.pop()

            if curr:
                if visited:
                    result.append(curr.val)
                else:
                    stack.append(curr)
                    v.append(True)
                    stack.append(curr.right)
                    v.append(False)
                    stack.append(curr.left)
                    v.append(False)
            
        return result

        