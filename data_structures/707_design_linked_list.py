## https://leetcode.com/problems/design-linked-list/

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        current = self.head

        for _ in range(0, index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be
        the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked
        list, the node will be appended to the end of linked list. If index is greater than the length, the node will not
        be inserted.
        """
        if index > self.size:
            return

        current = self.head
        new_node = ListNode(val)

        if index <= 0:
            new_node.next = current
            self.head = new_node
        else:
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        current = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                current = current.next
            current.next = current.next.next

        self.size -= 1

# class ListNode:
    
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev
        
        
# class MyLinkedList:

#     def __init__(self, val=0, next=None, prev = None):
#         self.length, self.head, self.tail = 0, None, None
        
#     def find(self, index):
#         if (index << 1) <= self.length: # index <= length - index
#             pointer = self.head
#             for _ in range(index): 
#                 pointer = pointer.next
#         else:
#             pointer = self.tail
#             for _ in range(self.length - 1 - index): 
#                 pointer = pointer.prev
#         return pointer
#         # pointer = self.head
#         # # print("traversing find function")
#         # for _ in range(index-1):
#         #     # print(pointer.val)
#         #     pointer = pointer.next
#         # return pointer

        
#     def get(self, index: int) -> int:
#         if index >= self.length:
#             return -1
#         return self.find(index).val
        

#     def addAtHead(self, val: int) -> None:
#         if self.length == 0:
#             self.head = self.tail = ListNode(val)
#             self.length = 1
#             return
        
#         newNode = ListNode(val, self.head)
#         self.head.prev = newNode
#         self.head = newNode
#         self.length += 1

        
#     def addAtTail(self, val: int) -> None:
#         if self.length == 0:
#             self.head = self.tail = ListNode(val)
#             self.length = 1
#             return
        
#         newNode = ListNode(val, None, self.tail)
#         self.tail.next = newNode
#         self.tail = newNode
#         self.length += 1
        
#     def addAtIndex(self, index: int, val: int) -> None:
#         if index > self.length:
#             return 
#         elif index == self.length:
#             return self.addAtTail(val)
#         elif index == 0:
#             return self.addAtHead(val)
        
#         pointer = self.find(index)
#         newNode = ListNode(val, pointer, pointer.prev)
#         pointer.prev.next = pointer.prev = newNode
#         self.length += 1

#     def deleteAtIndex(self, index: int) -> None:
#         # print("delete function", index, self.length, self.head.val, self.tail.val)
#         if index > self.length:
#             return
#         if self.length == 1:
#             self.length, self.head, self.tail = 0, None, None
#             return
#         if index == 0:
#             self.head = self.head.next
#             self.head.prev = None
#             self.length -= 1
#             return 
#         elif index == self.length:
#             self.tail = self.tail.prev
#             self.tail.next = None
#             self.length -= 1
#             return
        
        
#         pointer = self.find(index)
#         # print(pointer.val, pointer)
#         if pointer.prev:
#             pointer.prev.next = pointer.next
#         if pointer.next:
#             pointer.next.prev = pointer.prev
#         self.length -= 1
        
            
        


# # Your MyLinkedList object will be instantiated and called as such:
# # obj = MyLinkedList()
# # param_1 = obj.get(index)
# # obj.addAtHead(val)
# # obj.addAtTail(val)
# # obj.addAtIndex(index,val)
# # obj.deleteAtIndex(index)
