# https://leetcode.com/problems/middle-of-the-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## Fast solution: Only 1 traversal
        node = head
        while head and head.next:
            # print(node, head)
            node = node.next
            head = head.next.next
        return node
        
        ## Basic solution: O(N) + O(N/2) = O(N)
#         node = head
#         len = 0
#         while node!=None:
#             node = node.next
#             len += 1
#         # print(len, head)
        
#         target = len//2 + 1
#         for i in range(1,target):
#             # print(i, target, head)
#             head = head.next
#         return head
