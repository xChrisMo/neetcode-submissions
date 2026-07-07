# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # to check if height diff > 1
        balanced = True

        def dfs(root):
            # nonlocal import
            nonlocal balanced

            # base condition from leaf node
            if not root: return 0

            # recurse left and right
            left = dfs(root.left)
            right = dfs(root.right)
            
            # check if difference is more than 1 only when we do have a difference of more than 1!
            calc = abs(left - right)

            if calc > 1:
                balanced = False

            # this is to get the height for ever node from the base!
            return 1 + max(left, right)

        dfs(root)
        return balanced