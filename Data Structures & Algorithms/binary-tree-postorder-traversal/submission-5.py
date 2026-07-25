# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # out = []

        # def dfs(root):
        #     if not root: return []

        #     #left, right, add to out
        #     dfs(root.left)
        #     dfs(root.right)
        #     out.append(root.val)

        # dfs(root)
        # return out

        # stack traversal would be this,. since it is LIFO, if we want our terminal nodes first
        # we add every element seen to stack, 
        # bascially, out.append(curr.val)
        # go left, then go right.

        curr = root
        stack = []
        out = []

        # do preorder, flip and return ! 

        # while curr or stack, 
        # while curr:see wh
        # stack.append(curr.val)
        # curr = curr.left
        # move right?? not sure

        # when we breka out of the loop, we pop stack
        # append the popped value to res, 

        # while we have the stack 
        while curr or stack:
            while curr:

                # add current to stack to make LIFO work. 
                # so the first would become last
                out.append(curr.val)
                stack.append(curr)
                # keep exploring right 
                curr = curr.right
                # explore right

            curr = stack.pop()
            curr = curr.left

        return out[::-1]
                # 


        # [4566731]
        # [124]

