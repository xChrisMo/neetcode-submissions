# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Inorder = Left, Node, Right

        if not root: return []
        out = []

        def dfs(root):
            if root.left:
                dfs(root.left)

            out.append(root.val)

            if root.right:
                dfs(root.right)

        dfs(root)
        return out