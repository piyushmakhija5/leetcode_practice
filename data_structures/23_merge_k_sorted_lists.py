## https://leetcode.com/problems/merge-k-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    ## O(NlogN) solution using sorting
        if not lists:
            return None
        elif len(lists)==1:
            return lists[0]
        
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


    ## O(kN) time complexity --> too slow, O(1) space complexity
    #     if not lists:
    #         return None
    #     if len(lists)==1:
    #         return lists[0]

    #     for i in range(1,len(lists)):
    #         # print(i, lists[i])
    #         if i ==1:
    #             ans = self.merge2Lists(lists[i-1], lists[i])
    #         else:
    #             ans = self.merge2Lists(ans,lists[i])
    #     return ans

    # def merge2Lists(self, l,r):
    #     curr = temp = ListNode(-1)
    #     while l or r:
    #         if not l:
    #             curr.next = r
    #             r = r.next
    #         elif not r:
    #             curr.next = l
    #             l = l.next
    #         elif l.val <= r.val:
    #             curr.next = l
    #             l = l.next
    #         else:
    #             curr.next = r
    #             r = r.next
    #         curr = curr.next
    #     return temp.next
