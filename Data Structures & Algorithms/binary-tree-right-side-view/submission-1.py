# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        result = []
        level = 0
        if not root:
            return result
        queue.append(root)

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if level == len(result):
                    result.append(node.val)

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)
            level +=1
 
        return result
        