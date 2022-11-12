https://leetcode.com/problems/remove-linked-list-elements/

def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ## Working solution
        prev = dummy = ListNode(-1, head)
        while head:
            # print(prev)
            if head.val != val:
                prev = head
            else:
                prev.next = head.next
            head = head.next
        return dummy.next
            
        ## Less variables used here, but slower
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
