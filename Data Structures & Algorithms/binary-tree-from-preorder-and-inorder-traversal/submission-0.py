# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: add_to_arr, left, right
        # inorder: left, add_to_arr, right
        

        # find first of preorder, which is the root inside inorder,
        # get the count of left AND right, both sides of root_preorder inside inorder
        if not preorder or not inorder:
            return None

        mid = preorder[0]
        root = TreeNode(mid)
        find_root = inorder.index(mid)
        
        # preorder = [1, 2, 4, 5, 3, 6], 
        # inorder = [4, 2, 5, 1, 3, 6]

        # root = 1
        # index = inorder.index(1)

        # left = build(preorder[1:1+index:], inorder[:index])
        # right = build(preorder[1+index:], inorder[index+1:])

        root.left = self.buildTree(preorder[1:find_root+1], inorder[:find_root])
        root.right = self.buildTree(preorder[find_root+1:], inorder[find_root + 1:])


        return root