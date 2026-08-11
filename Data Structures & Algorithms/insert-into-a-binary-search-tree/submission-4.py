# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(cur):
            node = TreeNode(val)
            if not cur:
                # base case
                return node

            if val < cur.val:
                cur.left = dfs(cur.left)

            elif val > cur.val:
                cur.right = dfs(cur.right)

            return cur
            
        return dfs(root)