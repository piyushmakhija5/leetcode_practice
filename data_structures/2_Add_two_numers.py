## https://leetcode.com/problems/add-two-numbers/
## NEED TO PRACTICE THIS AGAIN !! ---> DONE !! Solution below
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ## O(N) solution
        res = ListNode(-1)
        cur = res
        carry = False
        while l1 or l2 or carry:
            ## Calculating carry            
            if carry:
                tmp = 1
                carry = False
            else: 
                tmp = 0
            
            ## Computing sum of current Nodes
            if not l1 and l2:
                valSum = tmp + l2.val
                l2 = l2.next
            elif not l2 and l1:
                valSum = tmp + l1.val
                l1 = l1.next
            elif l1 and l2:
                valSum = tmp+ l1.val+l2.val
                l1 = l1.next
                l2 = l2.next
            else:
                valSum = tmp
                
            ## Adding next node to result LL
            if valSum < 10:
                # print("sum less than 10")
                tmpNode = ListNode(val=valSum)
            else:
                # print("sum more than 10", (valSum)%10)
                tmpNode = ListNode(val=(valSum)%10)
                carry = True

            cur.next = tmpNode
            cur = cur.next
        return res.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 or l2 or carry:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum //10
            newNode = ListNode(columnSum %10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next
        ## O(max(m,n))
  
