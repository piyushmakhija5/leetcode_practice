## https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ## slow, fast pointer or two pointer solution
        fast, slow = head, head
        for _ in range(n): 
            fast = fast.next
        if not fast: 
            return head.next
        while fast.next: 
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head
        
        ## Own solution: bad algo
#         if not head:
#             return head
#         if not head.next:
#             return None
        
#         curr = head
#         l = 0
#         while curr:
#             curr = curr.next
#             l += 1
        
#         m = l - n
#         print(n,l,m)
        
#         prev = fake = ListNode(0,head)
#         curr = head
#         cnt = 0
#         while curr:
#             if cnt != m:
#                 curr = curr.next
#                 prev = prev.next
#                 cnt += 1
#             else:
#                 curr = curr.next
#                 prev.next = curr
#                 break

#         return fake.next
