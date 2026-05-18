# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        prev = slow.next = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        front, back = head, prev
        while back:
            nextFront, nextBack = front.next, back.next
            front.next = back
            back.next = nextFront
            front, back = nextFront, nextBack
