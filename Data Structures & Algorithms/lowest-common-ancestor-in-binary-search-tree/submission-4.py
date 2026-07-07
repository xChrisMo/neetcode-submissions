# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def lca(root, p, q):
            while root:

                # if both p.val and q.val are less than the root. we look left
                if p.val < root.val and q.val < root.val:
                    root = root.left

                # if both p.val and q.val are greater than the root. we look right 
                elif p.val > root.val and q.val > root.val:
                    root = root.right

                # no more ways of moving
                else:
                    return root

        return lca(root, p, q)