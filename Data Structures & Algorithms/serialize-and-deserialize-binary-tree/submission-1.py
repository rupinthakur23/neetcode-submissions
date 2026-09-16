# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        def inorder(root):
            if not root:
                result.append('NA')
                return
            result.append(str(root.val))
            inorder(root.left)
            inorder(root.right)
        inorder(root)
        
        return ','.join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(',')
        self.idx = 0

        def dfs():
            if values[self.idx] == 'NA':
                self.idx +=1
                return

            item = values[self.idx]
            self.idx +=1
            root = TreeNode(item)

            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()




