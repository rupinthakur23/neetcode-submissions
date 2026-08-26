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
        curr = head
        randomMap = {None: None}


        while curr:
            copy = Node(curr.val)
            randomMap[curr] = copy
            curr = curr.next
        
        curr = head

        while curr:
            copy = randomMap[curr]
            copy.next = randomMap[curr.next]
            copy.random = randomMap[curr.random]
            curr = curr.next

        
        return randomMap[head]
