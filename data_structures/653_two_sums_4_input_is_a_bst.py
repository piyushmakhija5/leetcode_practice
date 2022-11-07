## https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        ## Iterative solution leveraging BST properties
        def pushLeft(st, root):
            while root:
                st.append(root)
                root = root.left
                
        def pushRight(st, root):
            while root:
                st.append(root)
                root = root.right
                
        def nextLeft(st):
            node = st.pop()
            pushLeft(st, node.right)
            return node.val
        
        def nextRight(st):
            node = st.pop()
            pushRight(st, node.left)
            return node.val
        
        stLeft, stRight = [], []
        pushLeft(stLeft, root)
        pushRight(stRight, root)
        
        left, right = nextLeft(stLeft), nextRight(stRight)
        while left < right:
            if left + right == k:
                return True
            if left + right < k:
                left = nextLeft(stLeft)
            else:
                right = nextRight(stRight)
        return False
        
        
        
        ## Recursive DFS solution 1 using hashset. Does not take advantage of BST properties
#         def dfs(root, seen):
#             if not root:
#                 return False
#             complement = k - root.val
#             if complement in seen:
#                 return True
#             seen.add(root.val)
#             return dfs(root.left, seen) or dfs(root.right, seen)
#         return dfs(root, set())
                
