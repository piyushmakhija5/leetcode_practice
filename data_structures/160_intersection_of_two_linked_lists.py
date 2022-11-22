## https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ## O(1) space complexity solution, O(N+M) time complexity
        # a,b = headA, headB
        # while(a!=b):
        #     a = headB if not a else a.next
        #     b = headA if not b else b.next
        # return a
        
        ## O(N+M) time complexity, O(N) space complxity
        first = set()
        curr = headA
        while curr:
            first.add(curr)
            curr = curr.next

        curr = headB
        while curr:
            if curr in first:
                return curr
            curr = curr.next
        return None
        
        ## Too Slow: O(N)^2 Time complexity solution, O(1) space complexity solution
#         if not headA or not headB:
#             return None
        
#         while headA:
#             if self.nodeInOtherList(headA, headB):
#                 return headA
#             else:
#                 headA = headA.next
#         return None
                
        
#     def nodeInOtherList(self, headA, headB):
#         while headB:
#             if headA == headB:
#                 return True
#             else:
#                 headB = headB.next
#         return False
