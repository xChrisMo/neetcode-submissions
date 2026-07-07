# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left, right, out

        if not root: return []
        out = []

        def dfs(root):
            if root.left:
                dfs(root.left)

            if root.right:
                dfs(root.right)

            out.append(root.val)
            
        dfs(root)
        return out