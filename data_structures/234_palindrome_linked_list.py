## https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ## slow, fast pointer
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
        
        ## Simple solution -- not so fast
#         if not head or not head.next:
#             return True
        
#         data = []
#         curr = head
#         while curr:
#             data.append(curr.val)
#             curr = curr.next
        
#         data_r = data[::-1]
#         print(data, data_r)
#         return data == data_r

