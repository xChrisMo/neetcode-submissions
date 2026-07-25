# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        q = deque()
        q.append([root, 1])
        max_count = float('-inf')


        while q:
            for _ in range(len(q)):
                node, count = q.popleft()
                max_count = max(max_count, count)

                if node.left:
                    q.append([node.left, count + 1])

                if node.right:
                    q.append([node.right, count + 1])


        return max_count