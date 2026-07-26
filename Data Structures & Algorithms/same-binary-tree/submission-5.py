# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # do a recursive check
        # if not p and not q, return True - both are terminal
        # if p and not q, return False
        # if q and not p, return True
        # recursively call dfs(p.left, q.left) and dfs(p.right, q.right)


        # def dfs(p, q):
        #     if not p and not q: return True

        #     if q and not p: return False

        #     if p and not q: return False

        #     if p.val != q.val: return False

        #     return dfs(p.left, q.left) and dfs(p.right, q.right)

        # return dfs(p, q)

        stack_p = [p]
        stack_q = [q]

        # if curr_p.val != curr.q.val: return False
        # if curr_p.left != curr_q.left: return False
        # if curr_p.right != curr_q.right: return False
        # 
        if not p and not q:
            return True

        if not p or not q:
            return False

        while stack_p and stack_q:
            curr_p = stack_p.pop()
            curr_q = stack_q.pop()

            if curr_p.val != curr_q.val: return False

            if bool(curr_p.right) != bool(curr_q.right):
                return False

            if bool(curr_p.left) != bool(curr_q.left):
                return False

            if curr_p.left and curr_q.left:
                stack_p.append(curr_p.left)
                stack_q.append(curr_q.left)

            if curr_p.right and curr_q.right:
                stack_p.append(curr_p.right)
                stack_q.append(curr_q.right)

        if stack_p:
            return False

        if stack_q:
            return False

        return True