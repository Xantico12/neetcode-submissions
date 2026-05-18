# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        N = length - n
        if N == 0:
            return head.next

        curr = head
        print("N", N)
        for i in range(length - 1):
            print("i:", i, "curr:", curr)
            if (i + 1) == N:
                curr.next = curr.next.next
                break
            curr = curr.next

        return head
