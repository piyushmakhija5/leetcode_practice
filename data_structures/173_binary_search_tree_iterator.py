## https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []
        self.count = 0
        while root:
            self.nodes.append(root)
            self.count += 1
            root = root.left
        

    def next(self) -> int:
        ret = self.nodes.pop()
        self.count -= 1
        cur = ret.right
        while cur:
            self.nodes.append(cur)
            self.count += 1
            cur = cur.left
        return ret.val

    def hasNext(self) -> bool:
        return self.count > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
