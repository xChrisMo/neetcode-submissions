# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # we want to express all in terms of [withRoot, withoutRoot]
        # to simulate picking or NOT picking...

        def dfs(root):
            # base condition, 
            if not root:
                return [0, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            withRoot = root.val + left[1] + right[1]
            withoutRoot = max(left) + max(right)

            return [withRoot, withoutRoot]

        ans = dfs(root)
        print(ans)
        return max(ans)