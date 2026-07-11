# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # root == entrance
        # it has to be recursive, meaning we return to each parent 

        def dfs(root):
            # robbed, not robbed
            if not root: return [0,0] # with, without!

            # for a root, max there would be the max at its left and its right!

            # returns up to its parent somehow
            left = dfs(root.left)
            right = dfs(root.right)
            
            # withRoot..
            withroot = root.val + left[1] + right[1]
            
            # without root
            without_root = max(left) + max(right)
            return [withroot, without_root]

            

        # call dfs once
        out = dfs(root)
        # return max_amt ever gotten!
        return max(out)