# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # since it is always unique, just find the nearest poisiton!
        new_node = TreeNode(val)

        if not root: return new_node

        # if val > root, it goes right
        # if val < root, it goes left
        # at the the end, it goes to the right of whatever element it stops!

        curr = root

        while True:
            if curr.val < val:
                if not curr.right:
                    curr.right = new_node
                    return root
                else:
                    curr = curr.right

            elif curr.val > val:
                if not curr.left:
                    curr.left = new_node
                    return root

                else:
                    curr = curr.left

            #insert t

