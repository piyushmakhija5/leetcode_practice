## https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ## Iterative solution
        res = []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res
        
        ## Concise: Recursive solution
        # if not root:
        #     return []
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
        
        ## Recursive solution
#         res = []
#         def inOrder(node):
#             if not node:
#                 return
#             inOrder(node.left)
#             res.append(node.val)
#             inOrder(node.right)
#         inOrder(root)
#         return res
        
