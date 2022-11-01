## https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## Even more optimized solution
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
    
    ## Optimized solution
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev
        ## Basic solution: 2*O(N) = O(N)
#         if not head or head.next == None:
#             return head
#         valList = []
#         node = head
#         while node != None:
#             valList.append(node.val)
#             node = node.next
        
#         node2 = head2 = ListNode(-1)
#         for i in valList[::-1]:
#             # print(i)
#             newNode = ListNode(i, None)
#             node2.next = newNode
#             node2 = node2.next
#         return head2.next
