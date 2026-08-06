# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, min_so_far, max_so_far):
            if not root:
                return True

            if not (min_so_far < root.val < max_so_far):
                return False

            return validate(root.left, min_so_far, root.val) and validate(root.right, root.val, max_so_far)

        return validate(root, float('-inf'), float('inf'))
            

        