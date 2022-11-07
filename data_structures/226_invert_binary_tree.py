## https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ## Iterative solution: Working
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root
        
        # ## Concise recursive solution
        # if root:
        #     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root
        
        ## DFS recursive solution
        # if not root:
        #     return root
        # temp = root.left
        # root.left = root.right
        # root.right = temp
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root

    
        ## Iterative solution: own try. Works BUT returns list instead of root node
#         if not root:
#             return root
        
#         ans = []
#         queue = [root]
#         while queue:
#             new_queue = []
#             for node in queue:
#                 ans.append(node.val)
#                 print(ans, queue)
#                 if node.right:
#                     new_queue.append(node.right)
#                 if node.left:
#                     new_queue.append(node.left)
#             queue = new_queue
#         return ans
