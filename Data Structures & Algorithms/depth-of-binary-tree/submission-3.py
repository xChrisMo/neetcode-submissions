# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            #base condition
            if not root: return 0

            #recursive left and right
            left = dfs(root.left)
            right = dfs(root.right)

            #max_d itself 
            max_d = max(left, right)
            
            #what to return to each node, regarding its left and right
            return 1 + max(left, right)

        return dfs(root)
        #return max_d