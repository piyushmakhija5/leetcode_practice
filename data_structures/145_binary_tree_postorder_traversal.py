## https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ## Iterative solution
        if not root:
            return []
        
        res = []
        stack = [root]
        while stack:
            curr = stack[-1]
            if not curr.left and not curr.right:
                stack.pop()
                res.append(curr.val)
            if curr.right:
                stack.append(curr.right)
                curr.right = None
            if curr.left:
                stack.append(curr.left)
                curr.left = None
        return res

        
        ## Recursive Solution
        # if not root:
        #     return []
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        
