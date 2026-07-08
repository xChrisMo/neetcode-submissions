# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # base case of if it is or is not none
        def valid(root, left_bound, right_bound):
            # no root == True
            if not root:
                return True

            # if we have a left, check it is less than val 
            # if a right, check it is greater than val
            if not (left_bound < root.val < right_bound):
                return False

            # for each node, check if both left and right are true
            return valid(root.left, left_bound, root.val) and valid(root.right, root.val, right_bound)


        return valid(root, float('-inf'), float('inf'))