# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # we want to find the maximum path of a root
        # basically max(max, root.val + left.val + right.val)...
        # this question is asking postorder processing of nodes
        self.max_val = float('-inf')

        def dfs(root):
            # if not root: return 0
            # left = dfs(root.left)
            # right = dfs(root.right)

            # self.max_val = max(self.max_val, root.val, left + right)
            # return max(root.val, 0)

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            
            left = max(left, 0)
            right = max(right, 0)

            self.max_val = max(self.max_val, root.val + left + right)


            return root.val + max(left, right, 0)

        dfs(root)
        return self.max_val