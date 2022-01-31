# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
        

    
## 2 runners 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # print(slow, fast)
            if slow == fast:
                return True
        return False   
    
## Slow Solution
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if head == None or head.next == None:
#             return False
#         else:
#             data = [head]
#             newPointer = head.next
#             while newPointer.next != None:
#                 if newPointer in data:
#                     print(newPointer.val, data)
#                     return True
#                 data.append(newPointer)
#                 newPointer = newPointer.next                    
#             return False