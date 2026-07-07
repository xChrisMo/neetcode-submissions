# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # for each level, add the last element to an out

        # base condition
        if not root: return []

        # out that stores each level
        out = []

        # use a queue to set up the bfs
        q = deque()
        q.append(root)

        # we do a bfs 
        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            # after loop is finished, we add only the last element, AFTER THE FOR LOOP
            out.append(node.val)

        return out