from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []

        if not root: return []

        # bfs
        # while len(q), for i in range(q): pop, if left-append, if right-append

        q = deque()
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()

                # if we have something left
                if node.left:
                    q.append(node.left)
                
                # if we have something right
                if node.right:
                    q.append(node.right)

                # add to each level
                level.append(node.val)

            # for each paretn, we create. new level and add it to our general 'out'
            out.append(level)

        return out