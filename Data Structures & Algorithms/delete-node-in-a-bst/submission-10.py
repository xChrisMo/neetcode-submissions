# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(root, key):
            if not root:
                return None

            if key < root.val:
                root.left = dfs(root.left, val)

            elif key > root.val:
                root.right = dfs(root.right, val)

            else:
                # go one step right
                # then go left
                
                if not root.left:
                    return root.right

                elif not root.right:
                    return root.left

                else:
                    cur = root.right

                    while cur.left:
                        cur = cur.left

                    cur.left = root.left

                    return root.right

            return root

        return dfs(root, key)

