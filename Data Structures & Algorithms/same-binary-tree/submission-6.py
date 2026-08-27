# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        several edge cases 
        if not p and not q: return true, its the same
        if just one of them is true, return False, not same
        if the values of the root are not the same , return False.
        then recursively check for eacj node
        '''
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False
        left= self.isSameTree(p.left,q.left)
        right=self.isSameTree(p.right,q.right)

        return left and right 
