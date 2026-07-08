# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # preorder dfs
        out = []
        def empty(root):
            if not root:
                return 

            if root.left:
                empty(root.left)
            out.append(root.val)
            if root.right:
                empty(root.right)

        empty(root)
        
        return out[k-1]