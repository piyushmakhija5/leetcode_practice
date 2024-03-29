## https://leetcode.com/problems/balanced-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 1
            lh = height(root.left)
            rh = height(root.right)
            
            if lh == -1 or rh==-1 or abs(lh-rh)>1:
                return -1
            return 1 + max(height(root.left), height(root.right))
        return height(root)!= -1
