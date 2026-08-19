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
        nodes = {}

        curr = head
        while(curr):
            copy = Node(curr.val)
            nodes[curr] = copy
            curr = curr.next
        
        curr = head

        while(curr):
            if(curr.next):
                nodes[curr].next = nodes[curr.next]
            if(curr.random):
                nodes[curr].random = nodes[curr.random]
            curr = curr.next

        return nodes[head] if head else None
        