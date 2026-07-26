# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # two BINARY trees
        # how do i approach this as it isnt even a binary tree ?
        # 
        
        # starting from the start of 'root', let us call this adam
        # we check if adam at any point is equla to start of subroots' start, zanga

        # if it isnt, we move on, but if it is, we start the iteration from there
        # so have to do some sort of finding...
        # and then do some sort of recursion from the finding's results

        # match fucntion
        def isSameTree(p, q):
            if not p and not q:
                return True

            if not p:
                return False

            if not q: 
                return False

            if p.val != q.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        # search function
        if not root: return False
        if not subRoot: return True

        if isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            