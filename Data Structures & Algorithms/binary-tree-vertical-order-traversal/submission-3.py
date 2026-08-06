# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        dict_root = defaultdict(list)

        q.append([root, 0])
        min_v = 0
        max_v = 0

        while q:
            for _ in range(len(q)):
                node, c = q.popleft()
                min_v = min(min_v, c)
                max_v = max(max_v, c)

                dict_root[c].append(node.val)

                if node.left:
                    q.append([node.left, c - 1])

                if node.right:
                    q.append([node.right, c + 1])

        out = []
        for i in range(min_v, max_v + 1):
            out.append(dict_root[i])

        return out

        