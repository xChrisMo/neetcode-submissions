# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # def dfs(root):
        #     if not root: return 0

        #     left = dfs(root.left)
        #     right = dfs(root.right)

        #     return max(left, right) + 1


        # return dfs(root)
        if not root: return 0

        stack = [(root, 1)]
        curr = root
        max_depth = 0
        while stack:
            curr, depth = stack.pop()
            max_depth = max(max_depth, depth)

            if curr.left:
                stack.append((curr.left, depth + 1))

            if curr.right:
                stack.append((curr.right, depth + 1))

            # after adding both left and right, IF they exist, add 1?


        return max_depth