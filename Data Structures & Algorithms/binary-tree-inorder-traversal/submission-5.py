# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # out = []
        # def dfs(root):
        #     # base case, nothing in there anymore
        #     if not root: return out

        #     # go left
        #     dfs(root.left)
            
        #     # out.append
        #     out.append(root.val)
            
        #     # go right
        #     dfs(root.right)

        # dfs(root)
        # return out

        out = []
        stack = []
        curr = root

        while curr or stack:
            # at the first iteration, only curr is true
            while curr:
                stack.append(curr) # add the curr node to the stack
                curr = curr.left # mpve tp the left
                # no more lefts to explore

            curr = stack.pop() # this is what would get the correct order to actually, so the first pop gets the actual node cos remember, we add the curr itself before the left 
            out.append(curr.val) # add the element to the out
            curr = curr.right # move right, inorder meaning left before right, no more lefts!

            # we no longer have curr, we popped all its 

        return out