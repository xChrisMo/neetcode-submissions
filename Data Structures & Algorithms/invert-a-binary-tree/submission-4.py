# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # we traverse to a node that doesnt have kids underneath..
        # then traverse 1 step up from there (basically, we go to where a node has ONLY leaf nodes)
        # when we get a parent before leaf, we swap

        def dfs(root):
            # base condition, if empty, stop
            if not root: 
                return None

            # if both kids exist, swap left for right, right for left
            root.left, root.right = root.right, root.left

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return root