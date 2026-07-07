# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            # base case, both empty
            if not p and not q:
                return True

            # only one empty
            if not p or not q:
                return False

            # # not equal on the left
            # if p.left != q.left:
            #     return False

            # # not equal on the right
            # if p.right != q.right:
            #     return False

            # value mismatch
            if p.val != q.val:
                return False

            # none of the others, return True
            # what we return to each node from its children
            return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p, q)