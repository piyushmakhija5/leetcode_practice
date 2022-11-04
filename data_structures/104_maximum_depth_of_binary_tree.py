## https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ## Iterative solution
        if not root:
            return 0
        queue = [(root,1)]
        res = 0
        while queue:
            root, nums = queue.pop()
            if not root.left and not root.right:
                res = max(res, nums)
            if root.left:
                queue.append((root.left, nums+1))
            if root.right:
                queue.append((root.right, nums+1))
        return res
        
        
        
        ## Recursive DFS solution: concise
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
        ## Recursive solution using DFS
        # def dfs(root,depth):
        #     if not root:
        #         return depth
        #     return max(dfs(root.left, depth+1), dfs(root.right, depth+1))
        # return dfs(root,0)
