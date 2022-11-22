## https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## O(N) solution
        curr = head
        prev = fake = ListNode(-111, head)

        while curr:
            # print(prev.val, curr.val, tmp)
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            if prev.next == curr:
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next
        return fake.next
