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
        dummyNode = Node(-1)
        curr = head
        randomMap = {}
        start = dummyNode

        while curr:
            start.next = Node(curr.val)
            start = start.next
            randomMap[curr] = start
            curr = curr.next
        
        curr, start = head, dummyNode.next

        while curr:
            if curr.random:
                start.random = randomMap[curr.random]
            start = start.next
            curr = curr.next

        
        return dummyNode.next
