## https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        else:
            data = []
            data.append(head)        
            listNode = head.next 
            while listNode.next is not None:
                # print(listNode.val)
                if listNode in data:
                    return listNode
                data.append(listNode)
                listNode = listNode.next
            return None