# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(cur):
            if not cur:
                return cur

            if cur.val > key:
                cur.left = dfs(cur.left)

            elif cur.val < key:
                cur.right = dfs(cur.right)

            else:
                if not cur.left:
                    return cur.right

                if not cur.right:
                    return cur.left

                new_root = cur.right

                while new_root.left:
                    new_root = new_root.left

                new_root.left = cur.left
                return cur.right
            
            return cur

        return dfs(root)