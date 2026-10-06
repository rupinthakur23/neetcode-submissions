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
        oldToNew = {None:None}
        curr = head
        dummy = Node(-1)
        newNode = dummy

        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        curr = head

        while curr:
            newNode.next = oldToNew[curr] 
            newNode.next.random = oldToNew[curr.random] 
            curr = curr.next
            newNode = newNode.next
        
        return dummy.next
