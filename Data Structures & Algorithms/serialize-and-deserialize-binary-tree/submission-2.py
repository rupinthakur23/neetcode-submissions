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

        def preorder(root):
            if not root:
                result.append('None')
                return
            result.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        result = ','.join(result)
        return result

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        self.idx = 0

        def dfs():
            if data[self.idx] == 'None':
                self.idx +=1
                return None

            rootValue = data[self.idx]
            root = TreeNode(rootValue)
            self.idx +=1

            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()
