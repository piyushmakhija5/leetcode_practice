## https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ## Iterative Soltuion
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ans
                
        ## Recursive solution
        # ans = []
        # def dfs(root):
        #     if not root:
        #         return
        #     ans.append(root.val)
        #     dfs(root.left)
        #     dfs(root.right)
        # dfs(root)
        # return ans
        
