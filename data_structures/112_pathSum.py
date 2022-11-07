## https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ## One liner Concise recursive solution
        return (root.val==targetSum) if (root and not root.left and not root.right) else (root and (self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)))
        
        ## Recursive solution
        # if not root:
        #     return False
        # if not root.left and not root.right and root.val == targetSum:
        #     return True
        # targetSum -= root.val
        # return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

    
        ## Poor attempt !!
        # def dfs(root, curSum):
        #     if root :
        #         print(root.val, curSum)
        #         curSum += root.val
        #         if not root.left and not root.right and (curSum == targetSum):
        #             return True
        #         return dfs(root.left, curSum) or dfs(root.right, curSum)
        #     return False
        # return dfs(root, curSum)
