# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        # make n out
        # make recursive function
        # if not root, add 'N'
        # else, add str(root.val)!

        # return ''.join(res)

        def dfs(root):
            # base condition
            if not root:
                res.append('N')
                return 

            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ','.join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        self.i = 0

        def dfs():
            if data[self.i] == 'N':
                self.i += 1
                return None

            root = TreeNode(int(data[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()

            return root
        # call dfs
        return dfs()
