## https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ## Iterative soltuion
        if not root:
            return True
        dq = collections.deque([(root.left, root.right)])
        # print(dq)
        while dq:
            r1, r2 = dq.popleft()
            # print(r1,r2)
            if not r1 and not r2:
                continue
            if not r1 or not r2:
                return False
            if r1.val != r2.val:
                return False
            dq.append((r1.left, r2.right))
            dq.append((r1.right, r2.left))
        return True
        
        
        ## Recursive Solution
#         def dfs(r1, r2):
#             if not r1 and not r2:
#                 return True
#             if not r1 or not r2:
#                 return False
#             return (r1.val==r2.val) and (dfs(r1.left, r2.right)) and (dfs(r1.right, r2.left))
            
#         return dfs(root.left, root.right) if root else True
