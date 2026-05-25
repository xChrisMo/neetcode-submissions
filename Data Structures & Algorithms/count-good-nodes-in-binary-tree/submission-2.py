# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        max_so_far = float('-inf')

        def dfs(root, max_so_far):
            nonlocal count

            if not root: return 0

            if root.val >= max_so_far:
                count += 1

            #before we look at any children!
            max_so_far = max(max_so_far, root.val)
            
            # gives this to parent up
            return dfs(root.left, max_so_far) + dfs(root.right, max_so_far)
            

        dfs(root, float('-inf'))
        return count