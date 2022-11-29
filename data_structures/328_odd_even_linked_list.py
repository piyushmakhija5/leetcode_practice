## https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        curr = head
        even = curr2 = head.next
        
        while curr2 and curr2.next:
            print(curr.val, curr2.val)
            curr.next = curr2.next
            curr = curr.next
            
            curr2.next = curr.next
            curr2 = curr2.next    
        curr.next = even
        return head
