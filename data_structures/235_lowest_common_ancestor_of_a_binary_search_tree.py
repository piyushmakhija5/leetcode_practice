## https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ## Iterative solution
        small = min(p.val, q.val)
        large = max(p.val, q.val)
        while root:
            if root.val > large:
                root = root.left
            elif root.val < small:
                root = root.right
            else:
                return root
        return None
        
        ## Another recursive solution
#         if not root or root==p or root==q:
#             return root
#         left = self.lowestCommonAncestor(root.left, p,q)
#         right = self.lowestCommonAncestor(root.right, p,q)
        
#         if left and right:
#             return root
#         elif left:
#             return left
#         elif right:
#             return right
        
        
        ## Recursive own solution
        # if not root:
        #     return root
        # if (p.val <= root.val <= q.val) or (q.val <= root.val <= p.val):
        #     return root
        # elif root.val > p.val and root.val > q.val:
        #     return self.lowestCommonAncestor(root.left, p,q)
        # elif root.val < p.val and root.val < q.val:
        #     return self.lowestCommonAncestor(root.right, p,q)
        
