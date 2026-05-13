# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev



# head = listNode(val=0, next=node1)
# node1 = listNode(val=1, next=node2)
# node2 = listNode(val=2, next=node3)
# node3 = listNode(val=3, next=None)
