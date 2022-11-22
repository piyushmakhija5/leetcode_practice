## https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next
            
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return self.next
        
        ## failed trial
#         fast = head
#         while fast and fast.next:
#             tmp = fast.next

#             fast.next = fast.next.next
#             tmp.next = fast
#             fast = tmp
#             print(fast, tmp, head)

#             fast = fast.next.next
#             print(fast)
#         return head
