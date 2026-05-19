"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeToCopy = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            nodeToCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = nodeToCopy[curr]
            copy.next = nodeToCopy[curr.next]
            copy.random = nodeToCopy[curr.random]
            curr = curr.next
        
        return nodeToCopy[head]