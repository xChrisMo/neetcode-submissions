# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # for every recursion, cehcek max seen so far, if root.val > max seen so far, 
        # increase good
        self.good = 0

        def dfs(root, max_seen):
            if not root:
                return max_seen

            if root.val >= max_seen:
                self.good += 1
                max_seen = root.val

            dfs(root.left, max_seen)
            dfs(root.right, max_seen)

        dfs(root, float('-inf'))
        return self.good