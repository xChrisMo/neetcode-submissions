# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        def dfs(root):
            # base case, nothing in there anymore
            if not root: return out

            # go left
            dfs(root.left)
            
            # out.append
            out.append(root.val)
            
            # go right
            dfs(root.right)

        dfs(root)
        return out