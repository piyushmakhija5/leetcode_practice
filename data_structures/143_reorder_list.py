## https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ## 2 pointer solution
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        
        ## find middle node:
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        n = slow.next
        slow.next = prev = None
        
        # Reverse the second half
        while n:
            tmp = n.next
            n.next = prev
            prev = n
            n = tmp
            
        slow = head
        
        # Join first and 2nd half
        while slow and prev:
            tmp1 = slow.next
            tmp2 = prev.next
            
            slow.next = prev
            prev.next = tmp1
            slow = tmp1
            prev = tmp2
        return head
        

        
        ## FAILED APPROACH
#         ## Need to create a reverse list while maintaining the original list and then merge both lists        
#         ## 1. Create a copy of original LL and retain it
#         ## but how???
#         ## 2. create reverse List
#         prev = None
#         curr = head
#         while curr.next:
#             next = curr.next
#             curr.next = prev
            
            
#             prev = curr
#             curr = next
#         curr.head = prev
    
#         print(self.head)
            
    
#         ## 3. merge both Lists
#         new = l1
#         while l1 or l2:
#             if l1.val != l2.val
#             store1 = l1.next
#             store2 = l2.next
            
#             new.next = l2
#             l1 = l1.next
#             l2 = l2.next
