"""

create a copy first

then create the link (random) else random might not be estalished yet)
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        copy = { None: None }

        curr = head
        while curr:
            value = Node(curr.val)
            copy[curr] = value
            curr = curr.next


        curr = head
        while curr:
            connect = copy[curr]
            connect.next = copy[curr.next]
            connect.random = copy[curr.random]
            curr = curr.next

        return copy[head]

        