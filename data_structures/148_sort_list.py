## https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
            
        vals.sort()
        
        curr = newHead = ListNode()
        for i in range(len(vals)):
            node = ListNode(vals[i])
            curr.next = node
            curr = curr.next
        
        return newHead.next
        
