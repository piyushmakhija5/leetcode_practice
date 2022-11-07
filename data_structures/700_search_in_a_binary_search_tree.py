## https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ## Iterative approach
        stack, subtree = [], None
        while True:
            while root:
                if root.val == val:
                    subtree = root
                stack.append(root)
                root = root.left
            if subtree:
                return subtree
            if not stack:
                return None
            root = stack.pop().right
                    
        
        ## Concise recursive working solution
        # if not root:
        #     return None
        # if root.val == val:
        #     return root
        # return self.searchBST(root.left,val) if (root.val>val) else self.searchBST(root.right, val)
        
        ## Recursive working solution
        # if not root:
        #     return None
        # if root.val == val:
        #     return root
        # elif root.val < val:
        #     return self.searchBST(root.right, val)
        # else:
        #     return self.searchBST(root.left, val)
